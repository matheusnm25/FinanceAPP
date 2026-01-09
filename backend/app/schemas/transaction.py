from pydantic import BaseModel
from datetime import date

class TransactionCreate(BaseModel):
    description: str
    amount: float
    type: str
    category: str
    date: date