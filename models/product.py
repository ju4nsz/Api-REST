from sqlalchemy import Column, Integer, String, DateTime, DECIMAL
from sqlalchemy.orm import relationship
from database.config import Base

class Product(Base):
    """
    Represents a product in the database.

    Attributes:
        product_id (int): The unique identifier for the product (primary key).
        name (str): The name of the product.
        description (str): The description of the product.
        price (DECIMAL): The price of the product.
        created_date (DateTime): The date and time when the product was created.
        stock (int): The current stock quantity of the product.

    Relationships:
        orders (List[Order]): List of orders associated with the product.
    """
    
    __tablename__ = "products"
    
    product_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(50), index=True)
    description = Column(String(150))
    price = Column(DECIMAL(7,2), index=True)
    created_date = Column(DateTime, index=True)
    stock = Column(Integer, index=True)
    
    orders = relationship("Order", back_populates="product")