from fastapi import Depends,HTTPException,status
from app.models.user_model import User

from app.dependencies.auth_dependency import get_current_user

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