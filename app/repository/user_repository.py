from app.models.user_model import User
from sqlalchemy import or_
from app.core.logger import logger
from sqlalchemy.orm import joinedload



def get_user_by_email_username_repository(db, email: str = None, username: str = None):
    query = db.query(User)
    if email and username:
        return query.filter(or_(User.email == email, User.username == username)).first()
    if email:
        return query.filter(User.email == email).first()
    if username:
        return query.filter(User.username == username).first()
    return None


def create_user_repository(db, user_data):
    db_user = User(**user_data)
    db.add(db_user)
    try:
        db.commit()
        db.refresh(db_user)
        return db_user
    except Exception as e:
        db.rollback()
        logger.error(f"Error occurred while creating user: {e}")
        raise Exception(f"Error occurred while creating user: {e}")


def get_user_by_id_repository(db, user_id: int):
    db_user =db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        logger.warning(f"User with ID {user_id} not found")
        return None
    db_user.department_name = db_user.department.department_name if db_user.department else None
    return db_user

def update_user_repository(db, user_id: int, db_user, user_data):
    # Check for duplicate email/username BEFORE updating
    
    
    for key, value in user_data.items():
        setattr(db_user, key, value)

    try:
        db.commit()
        db.refresh(db_user)
        logger.info(f"User updated successfully: {user_id}")
        return db_user
    except Exception as e:
        db.rollback()
        logger.error(f"Error occurred while updating user: {e}")
        raise Exception (f"Error occurred while updating user: {e}")


def delete_user_repository(db, db_user):
    try:
        db.delete(db_user)
        db.commit()
        return {"detail": "User deleted successfully"}
    except Exception as e:
        db.rollback()
        logger.error(f"Error occurred while deleting user: {e}")
        raise Exception(f"Error occurred while deleting user: {e}")

def get_all_users_repository(db):
    try:
        users = db.query(User).options(joinedload(User.department)).all()
        # users = db.query(User).all()
        logger.info(f"Retrieved all users successfully. Total users: {len(users)}")
        return users
    except Exception as e:
        logger.error(f"Error occurred while retrieving all users: {e}")
        raise Exception(f"Error occurred while retrieving all users: {e}")
