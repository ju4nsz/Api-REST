from database.config import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, DECIMAL
from sqlalchemy.orm import relationship

class Order(Base):
    
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