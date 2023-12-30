from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemes.user import User
from schemes.order import Order, OrderBase
from services.order import OrderService
from services.auth import AuthService
from database.get_db import get_db

order_router = APIRouter(
    prefix="/v1/orders",
    tags=["Orders"]
)

db: Session = Depends(get_db)

auth_service = AuthService(db=db)

@order_router.post("", response_model=Order)
def new_order(new_order: OrderBase, 
              user: User = Depends(auth_service.get_current_user),
              db: Session = Depends(get_db)):
    """
    Create a new order.

    Parameters:
    - `new_order` (OrderBase): The order details.
    - `user` (User): The authenticated user.
    - `db` (Session): The SQLAlchemy database session.

    Returns:
    - The created order.

    Raises:
    - HTTPException: If the product is not found or if the user already has an active order with the product.
    """
    
    user_username = user.username
    
    order_service = OrderService(db=db)
    
    return order_service.create_order(new_order=new_order, user_username=user_username)
    