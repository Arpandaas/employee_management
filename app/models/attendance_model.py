from sqlalchemy import Boolean, Column, Date, Float, Integer, String, DateTime, ForeignKey
from app.config.database import Base
from datetime import datetime,date
from sqlalchemy.orm import relationship

class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    attendance_date = Column(Date, nullable=False, default=date.today)
    check_in_time = Column(DateTime, nullable=False, default=datetime.utcnow)
    check_out_time = Column(DateTime, nullable=True)
    working_hours = Column(Float, nullable=True)  # Total hours worked in a day
    status = Column(String(20), nullable=False, default='Present')  # e.g., 'Present', 'Absent', 'On Leave'
    late_flag = Column(Boolean, nullable=False, default=False)  # e.g., 'Yes' or 'No'
    late_minutes = Column(Integer, nullable=True)  # Minutes late
    auto_check_out_flag = Column(Boolean, nullable=False, default=False)  # e.g., 'Yes' or 'No'
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    def __repr__(self):
        return f"<Attendance(id={self.id}, user_id={self.user_id}, date={self.attendance_date})>"


