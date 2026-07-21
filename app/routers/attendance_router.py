from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.attendance_schema import AttendanceSchema, AttendanceBaseSchema,AttendanceCheckout,AttendanceCheckoutResponseSchema
from app.config.database import get_db
from app.services.attendance_service import create_attendance_service, check_out_attendance_service
from app.dependencies.auth_dependency import get_current_user   


attendance = APIRouter(
    prefix="/attendance",
    tags=["Attendance"],
    dependencies=[Depends(get_current_user)]
)


@attendance.get("/createAttendance", response_model=AttendanceSchema)
def create_attendance(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return create_attendance_service(db, current_user)

@attendance.put("/checkoutAttendance",response_model=AttendanceCheckoutResponseSchema)
def check_out_attendance(
    check_out : AttendanceCheckout,
    db :Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return check_out_attendance_service(db,check_out,current_user)