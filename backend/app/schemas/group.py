from pydantic import BaseModel
from typing import Optional

class GroupBase(BaseModel):
    name: str
    company_id: int


class GroupCreate(GroupBase):
    pass


class GroupUpdate(BaseModel):
    name: Optional[str] = None


class GroupResponse(GroupBase):
    id: int

    class Config:
        from_attributes = True