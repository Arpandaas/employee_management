
from sqlalchemy import Column, Integer, String,DateTime, ForeignKey
from app.config.database import Base
from datetime import datetime
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    full_name = Column(String(100), nullable=False)
    hashed_password = Column(String(255), nullable=False)
    role = Column(String(50), nullable=False, default='employee')  # e.g., 'admin', 'employee'
    department_id = Column(Integer, ForeignKey("Department.id"),nullable=True, )  # Assuming a user can belong to a department
    department = relationship("Department", back_populates="users")  # Relationship to Department model
    phone_number = Column(String(20), nullable=True)
    address = Column(String(255), nullable=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}', role='{self.role}')>"
