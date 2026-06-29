

from app.core.logger import logger
from app.models.department_model import Department
from sqlalchemy.orm import relationship,selectinload


def get_dept(db,department_code):
    query = db.query(Department)
    return query.filter(Department.department_code==department_code).first()

def get_dept_by_id (db,department_id):
    query = db.query(Department)

    return query.filter(Department.id == department_id).first() 


def create_department_repository(db,dept_data):
    deptpartment_data = Department(**dept_data)
    db.add(deptpartment_data)
    try:
        db.commit()
        db.refresh(deptpartment_data)
        return deptpartment_data
    except Exception as e:
        db.rollback()
        logger.error("Error occurred while creating Department: {e}")
        raise Exception ("Error occurred while creating Department: {e}")

def update_department_repository(db,dept_id,dept_data,db_dept_data):
    for key,value in dept_data.items():
        setattr(db_dept_data,key,value)
    
    try:
        db.commit()
        db.refresh(db_dept_data)
        logger.info(f"updated succesfully department id is:{dept_id}")
        return db_dept_data

    except Exception as e:
        logger.error(f"An error ocurred during updating department.error is {e}")
        raise Exception("An error ocurred during updating department.error is {e}")


def delete_department_repository(db,db_dept_data):
    try:
        db.delete(db_dept_data)
        db.commit()
        logger.info(f"deleted succesfully department id is:{db_dept_data.id}")
    except Exception as e:
        logger.error(f"An error occurred during deleting department. Error is {e}")
        raise Exception("An error occurred during deleting department. Error is {e}")
    

def get_all_departments_repository(db):
    return db.query(Department).options(selectinload(Department.users)).all()