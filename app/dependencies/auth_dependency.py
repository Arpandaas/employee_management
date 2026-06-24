from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.config.database import get_db
from app.repository.user_repository import get_user_by_id_repository
from sqlalchemy.orm import Session

from app.utils.jwt_utils import verify_access_token 

security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db:Session = Depends(get_db)
):

    token = credentials.credentials

    payload = verify_access_token(token)

    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )
    print("payload----",payload)
    user = get_user_by_id_repository(db,payload['user_id'])

    return user