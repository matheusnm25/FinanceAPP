from sqlalchemy.orm import Session
from app.repository.user import UserRepository
from app.repository.company import CompanyRepository
from app.schemas.user import UserCreate, UserUpdate
from app.models.user import User


class UserService:
    def __init__(self, db: Session):
        self.db = db
        self.user_repo = UserRepository(db)
        self.company_repo = CompanyRepository(db)

    def create_user(self, data: UserCreate) -> User:
        # validação de regra
        if data.company_id and data.company:
            raise ValueError("Use company_id OR company, not both")

        if not data.company_id and not data.company:
            raise ValueError("You must provide company_id or company")

        # cria company nova (ID incremental automático)
        if data.company:
            company = self.company_repo.create(data.company.name)
            company_id = company.id  # 👈 ID gerado pelo banco
        else:
            company_id = data.company_id

        return self.user_repo.create(data, company_id)

    def get_user(self, user_id: int) -> User | None:
        return self.user_repo.get_by_id(user_id)

    def update_user(self, user_id: int, data: UserUpdate) -> User | None:
        return self.user_repo.update(user_id, data)

    def delete_user(self, user_id: int) -> User | None:
        return self.user_repo.delete_by_id(user_id)