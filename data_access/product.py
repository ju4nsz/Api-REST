from models.product import Product
from sqlalchemy.orm import Session
from schemes.product import ProductCreate

class ProductAccess:
    """
    Class to handle product-related database operations.

    Attributes:
        db (Session): The SQLAlchemy database session.
    """

    def __init__(self, db: Session) -> None:
        """
        Initialize ProductAccess with a database session.

        Parameters:
            db (Session): The SQLAlchemy database session.
        """
        
        self.db = db
        
    def get_products(self):
        """
        Retrieve all products from the database.

        Returns:
            List[Product]: A list of Product objects representing all products in the database.

        Note:
            This method executes a query to fetch all products from the database.
            Make sure the database session (`self.db`) is properly configured and committed.
        """
        
        return self.db.query(Product).all()

    def create_product(self, new_product: ProductCreate):
        """
        Create a new product in the database.

        Parameters:
            new_product (ProductCreate): Pydantic model representing the product to be created.

        Returns:
            Product: The created product.
        """
        
        db_product = Product(**new_product.dict())
        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product

    def get_product_by_name(self, name: str):
        """
        Retrieve a product from the database by name.

        Parameters:
            name (str): The name of the product to retrieve.

        Returns:
            Product: The product with the specified name.
        """
        
        return self.db.query(Product).filter(Product.name == name).first()
