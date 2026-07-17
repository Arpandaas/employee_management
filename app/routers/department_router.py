from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.schemas.department_schema import DepartmentBaseSchema,DepartmentSchema,UpdateDepartmentSchema
from app.services.department_service import create_department_service,get_department_service,update_department_service,delete_department_service,get_all_departments_service
from app.dependencies.permission_dependency import require_admin,require_admin_manager_or_self



dep = APIRouter(prefix="/department",tags=["department"])




@dep.get("/")
def department():
    return "Welcome to Department"


@dep.post("/create_department")
def create_department(
    depart_data: DepartmentBaseSchema,
    db: Session = Depends(get_db),
    current_user = Depends(require_admin)
):
    return create_department_service(db,depart_data)



@dep.get("/getDepartment/{department_id}",response_model=DepartmentSchema)
def getDepartment(
    department_id : int,
    db: Session = Depends(get_db)
):
    return get_department_service(db,department_id)
    
@dep.put("/updateDept/{department_id}",response_model=DepartmentSchema)
def update_department(
    department_id : int,
    department_data : UpdateDepartmentSchema,
    db:Session = Depends(get_db),
    get_user = Depends(require_admin)
):
    
    return update_department_service(db,department_id,department_data)
    


@dep.delete("/deleteDept/{department_id}",response_model=DepartmentSchema)
def delete_department(
    department_id : int,
    db:Session = Depends(get_db),
    current_user = Depends(require_admin)
):
    return delete_department_service(db,department_id)

@dep.get("/getAllDepartments",response_model=list[DepartmentSchema])
def get_all_departments(
    db:Session = Depends(get_db),
    current_user= Depends(require_admin_manager_or_self)
):
    return get_all_departments_service(db)