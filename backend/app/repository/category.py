from app.models.category import Category
from app.schemas.category import CategoryUpdate
from .base import BaseRepository

class CategoryRepository(BaseRepository):

    def get_by_id(self, category_id: int) -> Category | None:
        return (
            self.db.query(Category)
            .filter(Category.id == category_id)
            .first()
        )

    def list_by_company(self, company_id: int) -> list[Category]:
        return (
            self.db.query(Category)
            .filter(Category.company_id == company_id)
            .all()
        )

    def create(self, category: Category) -> Category:
        return self.add(category)

    def update(
        self,
        category_id: int,
        data: CategoryUpdate
    ) -> Category | None:
        category = self.get_by_id(category_id)
        if not category:
            return None

        update_data = data.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(category, field, value)

        self.db.commit()
        self.db.refresh(category)
        return category

    def delete_by_id(self, category_id: int) -> Category | None:
        category = self.get_by_id(category_id)
        if not category:
            return None

        self.delete(category)
        return category