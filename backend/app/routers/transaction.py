from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from datetime import date
from app.services.transaction import TransactionService
from app.schemas.transaction import (
    TransactionCreate,
    TransactionUpdate,
    TransactionResponse
)
from app.database import get_db

router = APIRouter(prefix="/transactions", tags=["Transactions"])

@router.post("/", response_model=TransactionResponse)
def create_transaction(
    data: TransactionCreate,
    db: Session = Depends(get_db)
):
    return TransactionService(db).create_transaction(data)


@router.get("/{transaction_id}", response_model=TransactionResponse)
def get_transaction(
    transaction_id: int,
    db: Session = Depends(get_db)
):
    transaction = TransactionService(db).get_transaction(transaction_id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction


@router.get("/company/{company_id}", response_model=list[TransactionResponse])
def list_transactions_by_company(
    company_id: int,
    start_date: date | None = Query(None),
    end_date: date | None = Query(None),
    db: Session = Depends(get_db)
):
    return TransactionService(db).list_transactions_by_company(
        company_id, start_date, end_date
    )


@router.get("/user/{user_id}", response_model=list[TransactionResponse])
def list_transactions_by_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    return TransactionService(db).list_transactions_by_user(user_id)


@router.put("/{transaction_id}", response_model=TransactionResponse)
def update_transaction(
    transaction_id: int,
    data: TransactionUpdate,
    db: Session = Depends(get_db)
):
    transaction = TransactionService(db).update_transaction(transaction_id, data)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction


@router.delete("/{transaction_id}", response_model=TransactionResponse)
def delete_transaction(
    transaction_id: int,
    db: Session = Depends(get_db)
):
    transaction = TransactionService(db).delete_transaction(transaction_id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction