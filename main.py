import models
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from controllers.user import user_router
from controllers.product import product_router
from controllers.order import order_router
from database.config import engine
from database.get_db import get_db
from services.auth import AuthService

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/token")
async def login_for_token(form_data: OAuth2PasswordRequestForm = Depends(),
                          db: Session = Depends(get_db)):
    """
    Endpoint to obtain an access token (login).

    Parameters:
    - `form_data`: Form data with the username and password.
    - `db`: Database session.

    Returns:
    - Access token if the credentials are valid.
    """
    
    auth_service = AuthService(db=db)
    
    user = auth_service.authenticate_user(username=form_data.username, password=form_data.password)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
    access_token = auth_service.create_access_token(
        data={"sub": user.username}
    )
    
    return {"access_token": access_token, "token_type": "bearer"}    

app.include_router(user_router)
app.include_router(product_router)
app.include_router(order_router)