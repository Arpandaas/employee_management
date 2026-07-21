from datetime import timedelta

from app.core.logger import logger
from app.models.attendance_model import Attendance
from sqlalchemy.orm import relationship,selectinload


def create_attendance_repository(db,attendance_data):
    attendance = Attendance(**attendance_data)

    if attendance.check_in_time > timedelta(hours=9, minutes=30):
        attendance.late_flag = True
        attendance.late_minutes = (attendance.check_in_time - timedelta(hours=9, minutes=30)).seconds // 60
     
    db.add(attendance)
    db.commit()
    db.refresh(attendance)
    return attendance

def check_out_repository(db,check_out_dict):
    check_out_data = db.query(Attendance).filter(Attendance.user_id == check_out_dict["user_id"],
        Attendance.date == check_out_dict["date"]).first()
    if not check_out_data:
        return None
    if check_out_data.check_in_time is None:
        return None
    
    total_hours = check_out_dict["check_out_time"] - check_out_data.check_in_time
    check_out_data.check_out_time = check_out_dict["check_out_time"]
    if total_hours < timedelta(hours=4):
        check_out_data.status = "Absent"
    elif total_hours < timedelta(hours=8):
        check_out_data.status = "Half Day"  
    else:
        check_out_data.status = "Present"


    db.commit()
    db.refresh(check_out_data)
    return check_out_data