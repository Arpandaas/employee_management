from pydantic import BaseModel, ConfigDict, Field
from typing import Optional


class ManagerTeamSchema(BaseModel):
    id: int
    full_name: str
    username: str
    email: str
    department_id: Optional[int] = None
    department_name: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


class ManagerTeamResponse(BaseModel):
    total_no_of_team: int = Field(alias="total No of Team")
    employee: list[ManagerTeamSchema]

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)
