from sqlalchemy.orm import Session
from app.models.company import Company
from app.schemas.company import CompanyCreate, CompanyUpdate
from .base import BaseRepository


class CompanyRepository(BaseRepository):

    def get_by_id(self, company_id: int) -> Company | None:
        return (
            self.db.query(Company)
            .filter(Company.id == company_id)
            .first()
        )

    def list_all(self) -> list[Company]:
        return self.db.query(Company).all()

    def create(self, data: CompanyCreate) -> Company:
        """
        Cria uma nova company.
        O ID é gerado automaticamente pelo banco (incremental).
        """
        company = Company(**data.model_dump())
        self.db.add(company)
        self.db.flush()   # 🔥 força gerar company.id
        return company

    def update(
        self,
        company_id: int,
        data: CompanyUpdate
    ) -> Company | None:
        company = self.get_by_id(company_id)
        if not company:
            return None

        update_data = data.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(company, field, value)

        self.db.commit()
        self.db.refresh(company)
        return company

    def delete_by_id(self, company_id: int) -> Company | None:
        company = self.get_by_id(company_id)
        if not company:
            return None

        self.delete(company)
        return company