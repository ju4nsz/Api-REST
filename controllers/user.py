from fastapi import APIRouter, Depends
from services.user import UserService
from schemes.user import User, UserCreate
from database.get_db import get_db
from sqlalchemy.orm import Session

user_router = APIRouter()

@user_router.post("/v1/user", response_model=User)
def create_user(new_user: UserCreate, db: Session = Depends(get_db)):
    """
    Endpoint to create a new user.

    Parameters:
        new_user (UserCreate): Data for the new user to be created.
        db (Session): SQLAlchemy database session. Defaults to Depends(get_db).

    Returns:
        User: The created user.

    Raises:
        HTTPException: If a user with the same username or email already exists.
    """
    
    user_service = UserService(db=db)
    
    return user_service.create_user(new_user=new_user)