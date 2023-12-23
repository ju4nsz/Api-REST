from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    """
    Pydantic model for creating a new user.

    Attributes:
        username (str): The username of the user.
        password (str): The password of the user.
        email (EmailStr): The email address of the user.
        name (str): The name of the user.
        address (str): The address of the user.
    """
    
    username: str
    password: str
    email: EmailStr
    name: str
    address: str
    
class User(UserCreate):
    """
    Pydantic model representing a user.

    Attributes:
        user_id (int): The unique identifier for the user.
    """
    
    user_id: int
    
    class Config:
        """
        Pydantic configuration for ORM mode.
        """
        orm_mode = True
