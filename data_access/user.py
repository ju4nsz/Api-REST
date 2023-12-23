from pydantic import EmailStr
from sqlalchemy.orm import Session
from models.user import User
from schemes.user import UserCreate

class UserAccess:
    """
    Class to handle user-related database operations.

    Attributes:
        db (Session): The SQLAlchemy database session.
    """

    def __init__(self, db: Session):
        """
        Initialize UserAccess with a database session.

        Parameters:
            db (Session): The SQLAlchemy database session.
        """
        
        self.db = db

    def create_user(self, user: UserCreate):
        """
        Create a new user in the database.

        Parameters:
            user (UserCreate): Pydantic model representing the user to be created.

        Returns:
            User: The created user.
        """
        
        db_user = User(**user.dict())
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def get_user_by_username(self, username: str):
        """
        Retrieve a user from the database by username.

        Parameters:
            username (str): The username of the user to retrieve.

        Returns:
            User: The user with the specified username.
        """
        
        return self.db.query(User).filter(User.username == username).first()

    def get_user_by_email(self, email: EmailStr):
        """
        Retrieve a user from the database by email.

        Parameters:
            email (EmailStr): The email address of the user to retrieve.

        Returns:
            User: The user with the specified email address.
        """
        
        return self.db.query(User).filter(User.email == email).first()