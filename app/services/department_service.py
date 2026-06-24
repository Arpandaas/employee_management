from fastapi import HTTPException,status
from sqlalchemy.orm import Session

from app.repository.department_repository import get_dept,create_department_repository,get_dept_by_id,update_department_repository,delete_department_repository

def create_department_service(db,Dept_data):
    existing_dept = get_dept(db,Dept_data.department_code)

    if existing_dept :
        raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail="Already Present Department Code"
        )
    
    Dept_dict = {
        "department_name" : Dept_data.department_name,
        "department_code" : Dept_data.department_code,
        "details" : Dept_data.details
    }
    
    return create_department_repository(db,Dept_dict)

def get_department_service(db,dept_id):
    print('1111')
    dept_data = get_dept_by_id(db,dept_id)
    print(dept_data)
    if dept_data is None:
        raise HTTPException (
            status_code= status.HTTP_404_NOT_FOUND
        )
    return dept_data  

def update_department_service(
        db:Session,
        dept_id:int,
        dept_data
):
    db_dept_data = get_dept_by_id(db,dept_id)
    if db_dept_data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Department Not Found"
        )
    
    update_data = dept_data.model_dump(exclude_unset =True)
    new_dept_code = update_data.get('department_code',db_dept_data.department_code)
    if new_dept_code != db_dept_data.department_code :
        existing = get_dept(db,new_dept_code)
        if existing:
            raise HTTPException (
                status_code=status.HTTP_409_CONFLICT,
                detail="Already Present Department Code"
            )
        
    try :
            return update_department_repository(db,dept_id,update_data,db_dept_data)
    except Exception as e:

        raise HTTPException (
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error ocurred during updating department.error is {e}"
        )


def delete_department_service(db,dept_id):
    db_dept_data = get_dept_by_id(db,dept_id)
    if db_dept_data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Department Not Found"
        )
    
    try:
        delete_department_repository(db,db_dept_data)
        return {"message":"Department deleted successfully"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred during deleting department. Error is {e}"
        )