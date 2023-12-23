from fastapi import HTTPException, Depends
from schemes.user import UserCreate
from data_access.user import UserAccess
from sqlalchemy.orm import Session
from database.get_db import get_db

class UserService:
    """
    Class that encapsulates business logic related to users.

    Attributes:
        user_access (UserAccess): Object providing access to user-related database operations.
    """
    
    def __init__(self, db: Session):
        """
        Initializes the service with a database session.

        Parameters:
            db (Session): The database session.
        """
        self.user_access = UserAccess(db=db)
        
    def create_user(self, new_user: UserCreate):
        """
        Creates a new user if no user with the same username or email already exists.

        Parameters:
            new_user (UserCreate): Data for the new user to be created.

        Returns:
            User: The created user.
        
        Raises:
            HTTPException: If a user with the same username or email already exists.
        """
        
        user = self.user_access.get_user_by_username(username=new_user.username)
        if user:
            raise HTTPException(
                status_code=409,
                detail="Username already exists"
            )
            
        user = self.user_access.get_user_by_email(email=new_user.email)
        if user:
            raise HTTPException(
                status_code=409,
                detail="Email already exists"
            )
            
        db_user = self.user_access.create_user(user=new_user)
        return db_user

        
            
            
    
            
            
    
    