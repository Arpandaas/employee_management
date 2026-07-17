from fastapi import Depends,HTTPException,status
from sqlalchemy.orm import Session
from app.models.user_model import User
from app.config.database import get_db
from app.dependencies.auth_dependency import get_current_user
from app.services.user_service import get_user_by_id_repository


def require_admin(
       current_user : User= Depends(get_current_user)
):

    if current_user.role.lower() != 'admin':
        raise HTTPException (
            status_code=status.HTTP_403_FORBIDDEN,
            detail=" You are not authorized to access this resource. "
        )
    else:
        return current_user
    

def require_admin_or_self(
        user_id : int,
        current_user : User=Depends(get_current_user),
):
    if current_user.role.lower() != 'admin' and current_user.id != user_id :
        raise HTTPException (
            status_code =status.HTTP_403_FORBIDDEN,
            detail=" You are not authorized to access this resource. "
        )
    else:
        return current_user

def require_admin_manager_or_self(
        user_id : int,
        current_user: User =Depends(get_current_user),
        db:Session = Depends(get_db)

):
    requested_user = get_user_by_id_repository(db,user_id)

    if requested_user is None:
        raise HTTPException (
            status_code=status.HTTP_404_NOT_FOUND,
            detail=" No User Found"
        )
    role =current_user.role.lower()
    if role == 'admin' :
        return current_user
    elif role == 'manager' and requested_user.department_id == current_user.department_id  :
        return current_user
    elif current_user.id == user_id:
        return current_user
    else :
        raise HTTPException (
            status_code = status.HTTP_403_FORBIDDEN,
            detail= "You are not authorized to access this resource. "
        )


def require_admin_manager(
    current_user: User = Depends(get_current_user)
):
    if current_user.role.lower() == "manager":
        return current_user
    
    raise HTTPException (
            status_code = status.HTTP_403_FORBIDDEN,
            detail= "You are not authorized to access this resource. "
        )
