from datetime import date

from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repository.attendance_repository import create_attendance_repository, check_out_repository

def create_attendance_service(db: Session, current_user):
    attendance_dict = {
        "user_id": current_user.id,
        "date": date.today(),
        "status": "present",
        "check_in_time": date.today().strftime("%H:%M:%S")
    }
    atandance = create_attendance_repository(db, attendance_dict)    
    if atandance :
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail= "Attendence Not mark"
        )
    return {
    "message": "Check-in successful",
    "check_in": atandance.check_in_time,
    "status": atandance.status
}

def check_out_attendance_service(db: Session, check_out_data,current_user):
    check_out_dict = {
        "user_id" : current_user.id,
        "date": check_out_data.date,
        "check_out_time": check_out_data.check_out,
    }
    check_out = check_out_repository(db,check_out_dict)
    if check_out:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail= "Attendence Not mark"
        )
    return {
    "message": "Check-out successful",
    "check_in": check_out.check_out_time,
}