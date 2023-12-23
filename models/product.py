from database.config import Base
from sqlalchemy import Column, Integer, String, DateTime, DECIMAL
from sqlalchemy.orm import relationship

class Product(Base):
    
    __tablename__ = "products"
    
    product_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(50), index=True)
    description = Column(String(150))
    price = Column(DECIMAL(7,2), index=True)
    created_date = Column(DateTime, index=True)
    stock = Column(Integer, index=True)
    
    orders = relationship("Order", relationship="product")