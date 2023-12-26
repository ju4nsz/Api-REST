from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemes.user import User
from schemes.product import Product, ProductBase, ProductCreate
from services.auth import AuthService
from services.product import ProductService
from database.get_db import get_db

product_router = APIRouter(
    prefix="/product"
)

db: Session = Depends(get_db)

auth_service = AuthService(db=db)

@product_router.post("/v1/new", response_model=Product)
async def create_product(new_product: ProductBase, user: User = Depends(auth_service.get_current_user), 
                         db: Session = Depends(get_db)):
    
    """
    Create a new product.

    Parameters:
    - `new_product` (ProductBase): The base information for the new product.
    - `user` (User): The current authenticated user.
    - `db` (Session): The SQLAlchemy database session.

    Returns:
    - The created product.

    Raises:
    - HTTPException: If there is an issue creating the product.
    """
    
    new_product_with_date = ProductCreate(**new_product.dict(), created_date=datetime.utcnow())
    
    product_service = ProductService(db=db)
    
    return product_service.create_product(new_product=new_product_with_date)
    
    