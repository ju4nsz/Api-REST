from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, DECIMAL
from sqlalchemy.orm import relationship
from database.config import Base

class Order(Base):
    """
    Represents an order in the database.

    Attributes:
        order_id (int): The unique identifier for the order (primary key).
        user_id (int): The user ID associated with the order (foreign key).
        product_id (int): The product ID associated with the order (foreign key).
        order_date (DateTime): The date and time when the order was placed.
        dead_line (DateTime): The deadline for the order to be completed.
        status (str): The current status of the order.
        total (DECIMAL): The total cost of the order.
        notes (str): Additional notes or comments related to the order.

    Relationships:
        user (User): The user associated with the order.
        product (Product): The product associated with the order.
    """
    
    __tablename__ = "orders"
    
    order_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), index=True)
    product_id = Column(Integer, ForeignKey("products.product_id"), index=True)
    order_date = Column(DateTime, index=True)
    dead_line = Column(DateTime, index=True)
    status = Column(String(50), index=True)
    total = Column(DECIMAL(7,2))
    notes = Column(String(150))
    
    user = relationship("User", back_populates="orders")
    
    product = relationship("Product", back_populates="orders")