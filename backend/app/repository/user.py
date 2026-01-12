from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, data: UserCreate, company_id: int) -> User:
        user = User(
            name=data.name,
            email=data.email,
            is_active=data.is_active,
            permission_id=data.permission_id,
            company_id=company_id,
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_by_id(self, user_id: int) -> User | None:
        return self.db.query(User).filter(User.id == user_id).first()

    def update(self, user_id: int, data: UserUpdate) -> User | None:
        user = self.get_by_id(user_id)
        if not user:
            return None

        for field, value in data.model_dump(exclude_unset=True).items():
            setattr(user, field, value)

        self.db.commit()
        self.db.refresh(user)
        return user

    def delete_by_id(self, user_id: int) -> User | None:
        user = self.get_by_id(user_id)
        if not user:
            return None

        self.db.delete(user)
        self.db.commit()
        return user