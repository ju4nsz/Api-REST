from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from data_access.product import ProductAccess
from schemes.product import ProductCreate

class ProductService:
    """
    Service class for product-related business logic and operations.

    Attributes:
        db (Session): The SQLAlchemy database session.
        product_access (ProductAccess): Instance of ProductAccess for database operations.
    """

    def __init__(self, db: Session) -> None:
        """
        Initialize ProductService with a database session.

        Parameters:
            db (Session): The SQLAlchemy database session.
        """
        
        self.db = db
        self.product_access = ProductAccess(db=db)

    def create_product(self, new_product: ProductCreate):
        """
        Create a new product, checking for duplicates.

        Parameters:
            new_product (ProductCreate): Pydantic model representing the product to be created.

        Returns:
            Product: The created product.

        Raises:
            HTTPException: If a product with the same name already exists.
        """
        
        db_product = self.product_access.get_product_by_name(name=new_product.name)

        if db_product:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Product with the name {new_product.name} already exists"
            )

        return self.product_access.create_product(new_product=new_product)
    
    def get_products(self):
        """
        Retrieve all products from the database.

        Returns:
            List[Product]: A list of products retrieved from the database.
        """
        
        return self.product_access.get_products()
