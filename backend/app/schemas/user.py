from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    name: str
    email: EmailStr
    is_active: bool = True
    company_id: int
    permission_id: int


class CompanyCreate(BaseModel):
    name: str


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    is_active: bool = True
    permission_id: int

    # escolha de company
    company_id: Optional[int] = None
    company: Optional[CompanyCreate] = None


class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = None
    permission_id: Optional[int] = None


class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True