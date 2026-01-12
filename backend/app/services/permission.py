from sqlalchemy.orm import Session
from app.repository.permission import PermissionRepository
from app.schemas.permission import PermissionCreate, PermissionUpdate
from app.models.permission import Permission

class PermissionService:

    def __init__(self, db: Session):
        self.repo = PermissionRepository(db)

    def create_permission(self, data: PermissionCreate) -> Permission:
        return self.repo.create(data)

    def list_permissions(self) -> list[Permission]:
        return self.repo.list_all()

    def update_permission(
        self,
        permission_id: int,
        data: PermissionUpdate
    ) -> Permission | None:
        return self.repo.update(permission_id, data)

    def delete_permission(self, permission_id: int) -> Permission | None:
        return self.repo.delete_by_id(permission_id)