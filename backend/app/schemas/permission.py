from pydantic import BaseModel
from typing import Optional

class PermissionBase(BaseModel):
    name: str


class PermissionCreate(PermissionBase):
    pass


class PermissionUpdate(BaseModel):
    name: Optional[str] = None


class PermissionResponse(PermissionBase):
    id: int

    class Config:
        from_attributes = True