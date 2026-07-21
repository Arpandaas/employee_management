

from pydantic import BaseModel
from datetime import date, datetime


class AttendanceBaseSchema(BaseModel):
    date: date
    check_in: datetime

class AttendanceSchema(AttendanceBaseSchema):
    
    class Config:
        orm_mode = True

class AttendanceCheckout(BaseModel):
    employee_id: int
    date: date
    check_out: datetime
    class Config:
        orm_mode = True

class AttendanceResponseSchema(BaseModel):
    message: str
    check_in: datetime
    status: str

    class Config:
        orm_mode = True

class AttendanceCheckoutResponseSchema(BaseModel):
    message: str
    check_out: datetime

    class Config:
        orm_mode = True