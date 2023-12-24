import models
from fastapi import FastAPI
from controllers.user import user_router
from database.config import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_router)