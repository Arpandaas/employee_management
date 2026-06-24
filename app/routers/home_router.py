
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.schemas.user_schema import TokenResponseSchema,LoginSchema,UserCreateSchema
from app.services.user_service import login_user_service,create_user_service



home_router = APIRouter(
    prefix="/auth",
    tags=['auth']
)


@home_router.get("/")
def read_root():
    return {"message": "Welcome to the Employee Management System API!"}


@home_router.post("/login", response_model=TokenResponseSchema)
def login_user(
    login_data: LoginSchema,
    db: Session = Depends(get_db)
):
    return login_user_service(db, login_data)




@home_router.post("/create")
def create_user(
    user_data:  UserCreateSchema,
    db: Session = Depends(get_db),
):
    return create_user_service(db, user_data)
    
