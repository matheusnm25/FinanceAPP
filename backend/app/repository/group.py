from app.models.group import Group
from app.schemas.group import GroupUpdate
from .base import BaseRepository

class GroupRepository(BaseRepository):

    def get_by_id(self, group_id: int) -> Group | None:
        return (
            self.db.query(Group)
            .filter(Group.id == group_id)
            .first()
        )

    def list_by_company(self, company_id: int) -> list[Group]:
        return (
            self.db.query(Group)
            .filter(Group.company_id == company_id)
            .all()
        )

    def create(self, group: Group) -> Group:
        return self.add(group)

    def update(
        self,
        group_id: int,
        data: GroupUpdate
    ) -> Group | None:
        group = self.get_by_id(group_id)
        if not group:
            return None

        update_data = data.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(group, field, value)

        self.db.commit()
        self.db.refresh(group)
        return group

    def delete_by_id(self, group_id: int) -> Group | None:
        group = self.get_by_id(group_id)
        if not group:
            return None

        self.delete(group)
        return group