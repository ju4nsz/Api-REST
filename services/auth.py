from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from data_access.user import UserAccess
from passlib.context import CryptContext
from jose import jwt, JWTError
from os import getenv
from dotenv import load_dotenv
from schemes.token import TokenData
from datetime import timedelta, datetime

load_dotenv()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

class AuthService:
    """
    Service class for user authentication and token management.
    """

    def __init__(self, db: Session) -> None:
        """
        Initializes the AuthService with the database session.

        Parameters:
        - `db`: SQLAlchemy database session.
        """
        
        self.crypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self.user_data_access = UserAccess(db=db)
        
    def verify_password(self, password: str, db_password: str):
        """
        Verifies the provided password against the stored hashed password.

        Parameters:
        - `password`: Password to be verified.
        - `db_password`: Hashed password stored in the database.

        Returns:
        - `True` if passwords match, `False` otherwise.
        """
        
        if password == db_password:
            return True
        return False
        
    def authenticate_user(self, username: str, password: str):
        """
        Authenticates a user based on the provided username and password.

        Parameters:
        - `username`: Username of the user.
        - `password`: Password for authentication.

        Returns:
        - User object if authentication is successful, `None` otherwise.
        """
        
        user = self.user_data_access.get_user_by_username(username=username)
        
        if not user or not self.verify_password(password, user.password):
            return None
        
        return user
    
    async def decode_token(self, token: str):
        """
        Decodes a JWT token and verifies its validity.

        Parameters:
        - `token`: JWT token to be decoded.

        Returns:
        - Decoded payload if the token is valid.

        Raises:
        - HTTPException with 401 status if the token is not valid.
        """
        
        try:
            return jwt.decode(token, getenv("SECRET_KEY"), algorithms=["HS256"])
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
    
    def create_access_token(self, data: dict, expires_delta: timedelta | None = None):
        """
        Creates a JWT token with the provided data.

        Parameters:
        - `data`: Data to be encoded in the token.
        - `expires_delta`: Optional expiration time for the token.

        Returns:
        - Encoded JWT token.
        """
        
        to_encode = data.copy() if isinstance(data, dict) else {}
    
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
    
        to_encode.update({"exp": expire})
    
        encoded_jwt = jwt.encode(to_encode, getenv("SECRET_KEY"), algorithm="HS256")
        return encoded_jwt

    def get_current_user(self, token: str):
        """
        Retrieves the current user from the JWT token.

        Parameters:
        - `token`: JWT token containing user information.

        Returns:
        - TokenData object with the username.

        Raises:
        - HTTPException with 401 status if the token is not valid.
        """
        
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
        payload = jwt.decode(token, getenv("SECRET_KEY"), algorithms=["HS256"])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception    
            
        return TokenData(username=username)