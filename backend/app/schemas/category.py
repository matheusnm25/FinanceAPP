from pydantic import BaseModel
from typing import Optional

class CategoryBase(BaseModel):
    name: str
    company_id: int


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(BaseModel):
    name: Optional[str] = None


class CategoryResponse(CategoryBase):
    id: int

    class Config:
        from_attributes = True