
from fastapi import HTTPException, status
from app.repository.manager_repository import get_team_repository, get_team_by_id_repository
from app.schemas.manager_schema import ManagerTeamResponse


def get_team_service(db, dept_id: int):
    team = get_team_repository(db, dept_id)
    if not team:
        return ManagerTeamResponse(total_no_of_team=0, employee=[])
    for each in team:
        each.department_name = each.department.department_name

    total = len(team)
    return ManagerTeamResponse(total_no_of_team=total, employee=team)

def get_team_by_emp_id_service(db,emp_id:int):
    team = get_team_by_id_repository(db,emp_id)
    if not team:
        return ManagerTeamResponse(total_no_of_team=0, employee=[])
    team.department_name = team.department.department_name
    return team