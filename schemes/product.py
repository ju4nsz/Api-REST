from datetime import datetime
from pydantic import BaseModel

class ProductBase(BaseModel):
    """
    Pydantic model for the base attributes of a product.

    Attributes:
        name (str): The name of the product.
        description (str): The description of the product.
        price (float): The price of the product.
        stock (int): The current stock quantity of the product.
    """
    
    name: str
    description: str
    price: float
    stock: int
    
class ProductCreate(ProductBase):
    """
    Pydantic model for creating a new product.

    Attributes:
        created_date (datetime): The date and time when the product was created.
    """
    
    created_date: datetime
    
class Product(ProductCreate):
    """
    Pydantic model representing a product.

    Attributes:
        product_id (int): The unique identifier for the product.
    """
    
    product_id: int
    
    class Config:
        """
        Pydantic configuration for ORM mode.
        """
        orm_mode = True
