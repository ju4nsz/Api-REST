from database.config import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class User(Base):
    """
    Represents a user in the database.

    Attributes:
        user_id (int): The unique identifier for the user (primary key).
        username (str): The username of the user.
        password (str): The hashed password of the user.
        email (str): The email address of the user (unique).
        name (str): The name of the user.
        address (str): The address of the user.

    Relationships:
        orders (List[Order]): List of orders associated with the user.
    """
    
    __tablename__ = "users"
    
    user_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    username = Column(String(30), index=True, unique=True)
    password = Column(String(70))
    email = Column(String(50), unique=True, index=True)
    name = Column(String(50))
    address = Column(String(50))
    
    orders = relationship("Order", back_populates="user")