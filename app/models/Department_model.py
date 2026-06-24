from  sqlalchemy import Column,Integer,String,Text,DateTime
from  app.config.database import Base
from datetime import datetime
from sqlalchemy.orm import relationship

class Department(Base):
    __tablename__ = 'Department'
    id = Column(Integer,primary_key = True,index=True,autoincrement=True)

    department_name = Column(String(255),nullable=True)
    department_code = Column(String(20),index = True)
    details = Column(Text,nullable=True)
    users = relationship("User", back_populates="department")  # Relationship to User model
    created_at = Column(DateTime,nullable=False,default= datetime.now())
    updated_at = Column(DateTime,nullable = True,onupdate=datetime.now())

    def __repr__(self):
        return f"<Department(id={self.id}, department_name='{self.department_name}', department_code='{self.department_code}', details='{self.details}', created_at='{self.created_at}', updated_at='{self.updated_at}')>"
        

