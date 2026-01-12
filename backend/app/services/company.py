from sqlalchemy.orm import Session
from app.repository.company import CompanyRepository
from app.schemas.company import CompanyCreate, CompanyUpdate
from app.models.company import Company

class CompanyService:

    def __init__(self, db: Session):
        self.repo = CompanyRepository(db)

    def create_company(self, company: Company) -> Company:
        return self.repo.create(company)

    def get_company(self, company_id: int) -> Company | None:
        return self.repo.get_by_id(company_id)

    def list_companies(self) -> list[Company]:
        return self.repo.list_all()

    def update_company(
        self,
        company_id: int,
        data: CompanyUpdate
    ) -> Company | None:
        return self.repo.update(company_id, data)

    def delete_company(self, company_id: int) -> Company | None:
        return self.repo.delete_by_id(company_id)