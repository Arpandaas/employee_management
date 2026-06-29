
# from app.exceptions.custom_exception import UserNotFoundException
from app.exceptions.custom_exception import UserNotFoundException
from app.repository.user_repository import get_user_by_email_username_repository, create_user_repository, get_user_by_id_repository, update_user_repository, delete_user_repository, get_all_users_repository
from app.schemas.user_schema import TokenResponseSchema, UserCreateSchema, UserUpdateSchema, LoginSchema, LoginResponseSchema, UserResponseSchema    
from app.utils.hash_utils import hash_password, verify_password
from fastapi import HTTPException, status
from datetime import datetime
from sqlalchemy.orm import Session
from app.core.logger import logger
from app.utils.jwt_utils import create_access_token
from app.repository.department_repository import get_dept_by_id



def create_user_service(db:Session, user_data:UserCreateSchema):
    existing_user = get_user_by_email_username_repository(db, user_data.email, user_data.username)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email or username already registered"
        )
    user_dict = {
        "username": user_data.username,
        "email": user_data.email,
        "full_name": user_data.full_name,
        "hashed_password": hash_password(user_data.password),
        "role": user_data.role,
        "phone_number": user_data.phone_number,
        "address": user_data.address,
        "department_id": user_data.department_id,
        "created_at": datetime.now(),
        "updated_at": datetime.now()
    }

    logger.info(f"Creating user with email: {user_data.email} and username: {user_data.username}")
    return create_user_repository(db, user_dict)


def get_user_service(db:Session,user_id:int):
    
        db_user = get_user_by_id_repository(db, user_id)
        if  db_user is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        department_id = db_user.department_id
        if department_id is not None:
            department = get_dept_by_id(db, department_id)
            if department is None:
                logger.error(f"Department with ID {department_id} not found for user ID {user_id}")
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Department with ID {department_id} not found"
                )

        logger.info(f"Retrieving user with ID: {user_id}")
        return db_user
    
def update_user_service(db:Session, user_id:int, user_data:UserUpdateSchema):
    db_user = get_user_by_id_repository(db, user_id)

    if  db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    

    if user_data.password:
        user_data.password = hash_password(user_data.password)

    update_data = user_data.dict(exclude_unset=True)
    if "password" in update_data:
        update_data["hashed_password"] = update_data.pop("password")
    update_data["updated_at"] = datetime.now()

    logger.info(f"Updating user with ID: {user_id}")
    
    if 'username' in update_data or 'email' in update_data:
        new_username = update_data.get('username', db_user.username)
        new_email = update_data.get('email', db_user.email)
        
        # Check if new username already exists (for a different user)
        if new_username != db_user.username:
            existing = get_user_by_email_username_repository(db,None,new_username)
            if existing:
                logger.warning(f"Duplicate username attempt on update: {new_username}")
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="Username already exists"
                )
        
        # Check if new email already exists (for a different user)
        if new_email != db_user.email:
            existing = get_user_by_email_username_repository(db,new_email,None)
            if existing:
                logger.warning(f"Duplicate email attempt on update: {new_email}")
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="Email already exists"
       )
    try:
        return update_user_repository(db, user_id, db_user, update_data)
    except Exception as e:
        logger.error(f"Error occurred while updating user with ID {user_id}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while updating the user"+str(e)
        )

def delete_user_service(db:Session, user_id:int):
    db_user = get_user_by_id_repository(db, user_id)
    
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    try:
        logger.info(f"Deleting user with ID: {user_id}")  
        return delete_user_repository(db, db_user)
    except Exception as e:
        logger.error(f"Error occurred while deleting user with ID {user_id}: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while deleting the user"
        )
def login_user_service(db:Session, login_data: LoginSchema):
    user = get_user_by_email_username_repository(db, login_data.email, None)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid Credentials"
        )
    if not verify_password(login_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials")
    
    access_token = create_access_token(data={"user_id": user.id, "username": user.username, "email": user.email, "role": user.role})

    return TokenResponseSchema(access_token=access_token, token_type="bearer", message="Login successful")

def get_all_users_service(db: Session):
    users = get_all_users_repository(db)
    print(users)

    for user in users:
        if user.department_id is not None:
            user.department_name = user.department.department_name
    
    return users
        