from datetime import datetime
from pydantic import BaseModel

class OrderBase(BaseModel):
    """
    Pydantic model for the base attributes of an order.

    Attributes:
        user_id (int): The user ID associated with the order.
        product_id (int): The product ID associated with the order.
        notes (str | None): Additional notes or comments related to the order. It can be None.
    """
    
    user_id: int
    product_id: int
    notes: str | None
    
class OrderCreate(OrderBase):
    """
    Pydantic model for creating a new order.

    Attributes:
        order_date (datetime): The date and time when the order was placed.
        dead_line (datetime): The deadline for the order to be completed.
    """
    
    order_date: datetime
    dead_line: datetime
    
class Order(OrderCreate):
    """
    Pydantic model representing an order.

    Attributes:
        order_id (int): The unique identifier for the order.
        status (str): The current status of the order (default: "On the way").
        total (int): The total cost of the order.
        order_date (datetime): The date and time when the order was placed.
        dead_line (datetime): The deadline for the order to be completed.
    """
    
    order_id: int
    status: str = "On the way"
    total: int
    order_date: datetime
    dead_line: datetime
    
    class Config:
        """
        Pydantic configuration for ORM mode.
        """
        orm_mode = True