from database.config import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    
    user_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    username = Column(String(30), index=True, unique=True)
    password = Column(String(70))
    email = Column(String(50), unique=True, index=True)
    name = Column(String(50))
    adress = Column(String(50))
    
    orders = relationship("Order", back_populates="user")