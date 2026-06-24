from datetime import datetime
from pydantic import BaseModel,ConfigDict
from typing import Optional


# base Schema
class DepartmentBaseSchema(BaseModel):
    department_name:Optional['str'] =None
    department_code:str
    details:Optional['str'] =None


class DepartmentSchema(DepartmentBaseSchema):
    id : int
    created_at : datetime
    updated_at : Optional[datetime] =None

    model_config = ConfigDict(
        from_attributes  =True
    )

class UpdateDepartmentSchema(BaseModel):
    department_name:Optional['str'] =None
    department_code:Optional['str'] =None
    details:Optional['str'] =None