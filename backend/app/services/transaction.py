from sqlalchemy.orm import Session
from datetime import date
from app.repository.transaction import TransactionRepository
from app.schemas.transaction import TransactionCreate, TransactionUpdate
from app.models.transaction import Transaction

class TransactionService:
    def __init__(self, db: Session):
        self.repo = TransactionRepository(db)

    def create_transaction(self, transaction: Transaction) -> Transaction:
        # aqui você pode validar saldo, categoria, etc
        return self.repo.create(transaction)

    def get_transaction(self, transaction_id: int) -> Transaction | None:
        return self.repo.get_by_id(transaction_id)

    def list_transactions_by_company(
        self,
        company_id: int,
        start_date: date | None = None,
        end_date: date | None = None
    ) -> list[Transaction]:
        return self.repo.list_by_company(company_id, start_date, end_date)

    def list_transactions_by_user(self, user_id: int) -> list[Transaction]:
        return self.repo.list_by_user(user_id)

    def update_transaction(
        self,
        transaction_id: int,
        data: TransactionUpdate
    ) -> Transaction | None:
        return self.repo.update(transaction_id, data)

    def delete_transaction(self, transaction_id: int) -> Transaction | None:
        return self.repo.delete_by_id(transaction_id)