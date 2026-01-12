from sqlalchemy.orm import Session
from app.repository.group import GroupRepository
from app.schemas.group import GroupCreate, GroupUpdate
from app.models.group import Group

class GroupService:

    def __init__(self, db: Session):
        self.repo = GroupRepository(db)

    def create_group(self, group: Group) -> Group:
        return self.repo.create(group)

    def get_group(self, group_id: int) -> Group | None:
        return self.repo.get_by_id(group_id)

    def list_groups_by_company(self, company_id: int) -> list[Group]:
        return self.repo.list_by_company(company_id)

    def update_group(
        self,
        group_id: int,
        data: GroupUpdate
    ) -> Group | None:
        return self.repo.update(group_id, data)

    def delete_group(self, group_id: int) -> Group | None:
        return self.repo.delete_by_id(group_id)