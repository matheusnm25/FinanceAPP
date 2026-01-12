from datetime import date
from app.models.transaction import Transaction
from app.schemas.transaction import TransactionUpdate
from .base import BaseRepository

class TransactionRepository(BaseRepository):

    def get_by_id(self, transaction_id: int) -> Transaction | None:
        return (
            self.db.query(Transaction)
            .filter(Transaction.id == transaction_id)
            .first()
        )

    def list_by_company(
        self,
        company_id: int,
        start_date: date | None = None,
        end_date: date | None = None
    ) -> list[Transaction]:
        query = self.db.query(Transaction).filter(
            Transaction.company_id == company_id
        )

        if start_date:
            query = query.filter(Transaction.date >= start_date)

        if end_date:
            query = query.filter(Transaction.date <= end_date)

        return query.all()

    def list_by_user(self, user_id: int) -> list[Transaction]:
        return (
            self.db.query(Transaction)
            .filter(Transaction.user_id == user_id)
            .all()
        )

    def create(self, transaction: Transaction) -> Transaction:
        return self.add(transaction)

    def update(
        self,
        transaction_id: int,
        data: TransactionUpdate
    ) -> Transaction | None:
        transaction = self.get_by_id(transaction_id)
        if not transaction:
            return None

        update_data = data.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(transaction, field, value)

        self.db.commit()
        self.db.refresh(transaction)
        return transaction

    def delete_by_id(self, transaction_id: int) -> Transaction | None:
        transaction = self.get_by_id(transaction_id)
        if not transaction:
            return None

        self.delete(transaction)
        return transaction