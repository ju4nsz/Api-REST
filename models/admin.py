from database.config import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Admin(Base):
    """
    Represents an administrator in the database.

    Attributes:
        admin_id (int): The unique identifier for the administrator (primary key).
        username (str): The username of the administrator.
        email (str): The email address of the administrator (unique).

    Relationships:
        No relationships defined for the Admin class in this example.
    """
    
    __tablename__ = "admins"
    
    admin_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), index=True, unique=True)
    email = Column(String(50), index=True, unique=True)
    
    