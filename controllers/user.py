from fastapi import APIRouter, Depends
from services.user import UserService
from services.auth import AuthService
from schemes.user import User, UserCreate
from schemes.order import Order
from database.get_db import get_db
from sqlalchemy.orm import Session

user_router = APIRouter(
    prefix="/user"
)

@user_router.post("/v1/create", response_model=User)
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

@user_router.get("/v1/orders")
async def get_orders(user: User = Depends(AuthService().get_current_user), 
                     db: Session = Depends(get_db)):
    """
    Endpoint to retrieve orders for the authenticated user.

    Parameters:
    - `user`: Current user obtained from the JWT token.
    - `db`: SQLAlchemy database session.

    Returns:
    - List of orders associated with the authenticated user.

    Raises:
    - HTTPException: If there is an error retrieving the orders.
    """
    
    user_service = UserService(db=db)
    
    return await user_service.get_orders(username=user.username)