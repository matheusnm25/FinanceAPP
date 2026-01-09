from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.transaction import TransactionCreate
from app.models.transaction import Transaction

router = APIRouter(prefix="/transactions", tags=["Transactions"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_transaction(data: TransactionCreate, db: Session = Depends(get_db)):
    transaction = Transaction(**data.dict(), user_id=1)
    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return transaction