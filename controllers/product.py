from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemes.user import User
from schemes.product import Product, ProductBase, ProductCreate
from services.auth import AuthService
from services.product import ProductService
from database.get_db import get_db

product_router = APIRouter(
    prefix="/v1/product",
    tags=["Product"]
)

db: Session = Depends(get_db)

auth_service = AuthService(db=db)

@product_router.post("", response_model=Product)
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

@product_router.get("", response_model=List[Product])
def get_products(user: User = Depends(auth_service.get_current_user), 
                 db: Session = Depends(get_db)):
    """
    Retrieve all products.

    This endpoint requires authentication. Only authenticated users can access it.

    Args:
        user (User): The authenticated user obtained from the JWT token.
        db (Session): The SQLAlchemy database session.

    Returns:
        List[Product]: A list of products.

    Raises:
        HTTPException: Returns 401 UNAUTHORIZED if the user is not authenticated.
    """
    
    product_service = ProductService(db=db)
    
    return product_service.get_products()
    
    