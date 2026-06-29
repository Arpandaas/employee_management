from fastapi import FastAPI

from app.routers.home_router import home_router
from app.routers.user_router import router 
from app.config.database import engine, Base
from app.models.user_model import User
from app.models.department_model import Department
from app.exceptions.handlers import user_not_found_handler
from app.exceptions.custom_exception import UserNotFoundException
from app.routers.department_router import dep


# Create database tables
Base.metadata.create_all(bind=engine)


# Create the FastAPI app and include the router
app = FastAPI()
app.include_router(router)
app.include_router(home_router)
app.include_router(dep)
app.add_exception_handler(UserNotFoundException, user_not_found_handler)
# Run the app with: uvicorn main:app --reload

# database connection and model initialization
