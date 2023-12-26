from models.order import Order
from sqlalchemy.orm import Session
from schemes.order import OrderCreate

class OrderAccess:
    """
    Data access class for handling order-related database operations.

    Parameters:
    - `db` (Session): The SQLAlchemy database session.
    """
    
    def __init__(self, db: Session) -> None:
        """
        Initializes the OrderAccess.

        Parameters:
        - `db` (Session): The SQLAlchemy database session.
        """
        
        self.db = db
        
    def create_order(self, new_order: OrderCreate):
        """
        Creates a new order in the database.

        Parameters:
        - `new_order` (OrderCreate): The order details.

        Returns:
        - The created order.
        """
        
        db_order = Order(**new_order.dict())
        self.db.add(db_order)
        self.db.commit()
        self.db.refresh(db_order)
        return db_order
    
    def verify_order_of_user(self, user_username: str, product_name: str):
        """
        Verifies if a user has an active order with a specific product.

        Parameters:
        - `user_username` (str): The username of the user.
        - `product_name` (str): The name of the product.

        Returns:
        - The order if found, otherwise None.
        """
        
        return self.db.query(Order).filter(Order.user_username == user_username, Order.product_name == product_name).first()
