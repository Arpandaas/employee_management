from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, ConfigDict


# ==========================================
# Base Schema
# ==========================================
class UserBaseSchema(BaseModel):
    username: str
    email: EmailStr
    full_name: str
    role: Optional[str] = "employee"
    phone_number: Optional[str] = None
    address: Optional[str] = None


# ==========================================
# Create User Request
# ==========================================
class UserCreateSchema(UserBaseSchema):
    password: str
    department_id: Optional[int] = None


# ==========================================
# Update User Request
# ==========================================
class UserUpdateSchema(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    role: Optional[str] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None
    password: Optional[str] = None


# ==========================================
# User Response
# ==========================================
class UserResponseSchema(UserBaseSchema):
    id: int
    created_at: datetime
    updated_at: datetime
    department_id: Optional[int] = None
    department_name: Optional[str] = None  # Include department name in the response

    model_config = ConfigDict(
        from_attributes=True
    )


# ==========================================
# Login Request
# ==========================================
class LoginSchema(BaseModel):
    email: EmailStr
    password: str


# ==========================================
# Login Response
# ==========================================
class LoginResponseSchema(BaseModel):
    username: str
    email: EmailStr
    full_name: str
    role: str

    model_config = ConfigDict(
        from_attributes=True
    )

# =========================================
# Token Response
# =========================================
class TokenResponseSchema(BaseModel):
    access_token: str
    token_type: str = "bearer"
    message: Optional[str] = None
