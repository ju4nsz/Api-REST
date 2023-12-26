from datetime import datetime
from pydantic import BaseModel

class OrderBase(BaseModel):
    """
    Pydantic model for the base attributes of an order.

    Attributes:
        product_name (str): The product name associated with the order.
        notes (str | None): Additional notes or comments related to the order. It can be None.
    """
    
    
    product_name: str
    notes: str | None
    
class OrderCreate(OrderBase):
    """
    Pydantic model for creating a new order.

    Attributes:
        user_username (str): The username of the user associated with the order.
        order_date (datetime): The date and time when the order was placed.
        dead_line (datetime): The deadline for the order to be completed.
        status (str): The current status of the order (default: "On the way").
        total (int): The total cost of the order.
    """
    
    user_username: str
    order_date: datetime
    dead_line: datetime
    total: float
    status: str = "On the way"
    
class Order(OrderCreate):
    """
    Pydantic model representing an order.

    Attributes:
        order_id (int): The unique identifier for the order.
    """
    
    order_id: int
    
    class Config:
        """
        Pydantic configuration for ORM mode.
        """
        orm_mode = True