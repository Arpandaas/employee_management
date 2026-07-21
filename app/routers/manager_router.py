from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.manager_schema import ManagerTeamResponse
from app.dependencies.auth_dependency import get_current_user
from app.dependencies.permission_dependency import require_admin_manager
from app.config.database import get_db
from app.services.manager_service import get_team_service


manager = APIRouter(
    prefix="/manager",
    tags=["manager"],
    dependencies=[Depends(get_current_user)]

)

@manager.get("/getTeam/", response_model=ManagerTeamResponse)
def getTeam(
    db: Session = Depends(get_db),
    current_user=Depends(require_admin_manager)
):
    dept_id = current_user.department_id
    return get_team_service(db,dept_id)