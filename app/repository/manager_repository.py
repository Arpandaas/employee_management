from sqlalchemy.orm import joinedload

from app.models.user_model import User


def get_team_repository(db,dept_id:int):
    team = db.query(User).options(joinedload(User.department)).filter((User.department_id == dept_id) & (User.role =='employee')).all()
    return team


def get_team_by_id_repository(db,emp_id:int):
    team = db.query(User).options(joinedload(User.department)).filter((User.id == emp_id) & (User.role =='employee')).first()
    return team