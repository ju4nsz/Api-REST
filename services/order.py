from datetime import datetime, timedelta

from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from data_access.order import OrderAccess
from data_access.user import UserAccess
from data_access.product import ProductAccess
from schemes.order import OrderBase, OrderCreate
from models.order import Order

class OrderService:
    """
    Service class for handling order-related operations.

    Parameters:
    - `db` (Session): The SQLAlchemy database session.

    """
    
    def __init__(self, db: Session) -> None:
        """
        Initializes the OrderService.

        Parameters:
        - `db` (Session): The SQLAlchemy database session.

        """
        
        self.db  = db
        self.order_access = OrderAccess(db=db)
        self.user_access = UserAccess(db=db)
        self.product_accesss = ProductAccess(db=db)
        
    def create_order(self, new_order: OrderBase, user_username: str):
        """
        Creates a new order for a user.

        Parameters:
        - `new_order` (OrderBase): The order details.
        - `user_username` (str): The username of the user placing the order.

        Returns:
        - The created order.

        Raises:
        - HTTPException: If the product is not found or the user already has an active order with the product.
        """
        
        db_product = self.product_accesss.get_product_by_name(name=new_order.product_name)
        
        if not db_product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Product not found"
            )
            
        db_order = self.order_access.verify_order_of_user(user_username=user_username, product_name=new_order.product_name)
        
        if db_order:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="You already have an active order with this product"
            )
            
        order_date = datetime.utcnow()
        dead_line = order_date + timedelta(days=7)
            
        new_order_with_date = OrderCreate(**new_order.dict(), order_date=order_date, dead_line=dead_line, total=db_product.price, user_username=user_username)
        
        return self.order_access.create_order(new_order=new_order_with_date)