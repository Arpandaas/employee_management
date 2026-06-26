from datetime import datetime
from pydantic import BaseModel,ConfigDict
from typing import Optional

from app.schemas.user_schema import UserResponseSchema


# base Schema
class DepartmentBaseSchema(BaseModel):
    department_name:Optional['str'] =None
    department_code:str
    details:Optional['str'] =None


class DepartmentSchema(DepartmentBaseSchema):
    id : int
    created_at : datetime
    updated_at : Optional[datetime] =None
    users : Optional[list[UserResponseSchema]] = []  # Include users in the department
    

    model_config = ConfigDict(
        from_attributes  =True
    )
class DepartmentUserSchema(BaseModel):
    id : int
    username:str
    full_name:str
    email:str
    model_config = ConfigDict(
        from_attributes  =True
    )   

class UpdateDepartmentSchema(BaseModel):
    department_name:Optional['str'] =None
    department_code:Optional['str'] =None
    details:Optional['str'] =None
    