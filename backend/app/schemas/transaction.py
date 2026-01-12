from pydantic import BaseModel
from typing import Optional
from datetime import date

class TransactionBase(BaseModel):
    description: Optional[str] = None
    amount: float
    type: str  # income | expense
    currency: str
    date: date
    user_id: int
    company_id: int
    category_id: Optional[int] = None
    group_id: Optional[int] = None


class TransactionCreate(TransactionBase):
    pass


class TransactionUpdate(BaseModel):
    description: Optional[str] = None
    amount: Optional[float] = None
    type: Optional[str] = None
    currency: Optional[str] = None
    date: Optional[date] = None
    category_id: Optional[int] = None
    group_id: Optional[int] = None


class TransactionResponse(TransactionBase):
    id: int

    class Config:
        from_attributes = True