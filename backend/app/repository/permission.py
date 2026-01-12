from sqlalchemy.orm import Session
from app.models.permission import Permission
from app.schemas.permission import PermissionCreate, PermissionUpdate
from app.repository.base import BaseRepository

class PermissionRepository(BaseRepository):

    def __init__(self, db: Session):
        super().__init__(db)

    def create(self, data: PermissionCreate) -> Permission:
        permission = Permission(**data.model_dump())
        return self.add(permission)

    def get_by_id(self, permission_id: int) -> Permission | None:
        return (
            self.db.query(Permission)
            .filter(Permission.id == permission_id)
            .first()
        )

    def get_by_name(self, name: str) -> Permission | None:
        return (
            self.db.query(Permission)
            .filter(Permission.name == name)
            .first()
        )

    def list_all(self) -> list[Permission]:
        return self.db.query(Permission).all()

    def update(self, permission_id: int, data: PermissionUpdate) -> Permission | None:
        permission = self.get_by_id(permission_id)
        if not permission:
            return None

        update_data = data.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(permission, field, value)

        self.db.commit()
        self.db.refresh(permission)
        return permission

    def delete_by_id(self, permission_id: int) -> Permission | None:
        permission = self.get_by_id(permission_id)
        if not permission:
            return None

        self.delete(permission)
        return permission