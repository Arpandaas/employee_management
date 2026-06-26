from fastapi import Depends,HTTPException
from app.models.user_model import User

from app.dependencies.auth_dependency import get_current_user

def require_admin(
       current_user : User= Depends(get_current_user)
):

    if current_user.role.lower() != 'admin':
        raise HTTPException (
            status_code=403,
            detail=" Access denied"
        )
    else:
        return current_user