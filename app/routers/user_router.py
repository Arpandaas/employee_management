from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies.auth_dependency import get_current_user
from app.config.database import get_db
from app.schemas.user_schema import UserUpdateSchema,UserResponseSchema
from app.services.user_service import get_user_service,update_user_service,delete_user_service,get_all_users_service
from app.dependencies.permission_dependency import require_admin,require_admin_or_self

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    dependencies=[Depends(get_current_user)]
)






@router.get("/getUser/{user_id}", response_model=UserResponseSchema)
def read_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(require_admin_or_self)
):
    
    return get_user_service(db, user_id)


@router.put("/updateUser/{user_id}", response_model=UserResponseSchema)
def update_user(
    user_id: int,
    user_data: UserUpdateSchema,
    db: Session = Depends(get_db),
    current_user = Depends(require_admin_or_self)
):
    return update_user_service(db, user_id, user_data)


@router.delete("/deleteUser/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user = Depends(require_admin)
):

    return delete_user_service(db, user_id)


@router.get("/me",response_model=UserResponseSchema)
def get_me(
    current_user=Depends(get_current_user)
):
    return current_user


@router.get("/getAllUsers", response_model=list[UserResponseSchema])
def get_all_users(
    db: Session = Depends(get_db),
    current_user=Depends(require_admin)
):
    return get_all_users_service(db)