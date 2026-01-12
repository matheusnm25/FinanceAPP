from sqlalchemy.orm import Session
from app.repository.category import CategoryRepository
from app.schemas.category import CategoryCreate, CategoryUpdate
from app.models.category import Category

class CategoryService:

    def __init__(self, db: Session):
        self.repo = CategoryRepository(db)

    def create_category(self, category: Category) -> Category:
        return self.repo.create(category)

    def get_category(self, category_id: int) -> Category | None:
        return self.repo.get_by_id(category_id)

    def list_categories_by_company(self, company_id: int) -> list[Category]:
        return self.repo.list_by_company(company_id)

    def update_category(
        self,
        category_id: int,
        data: CategoryUpdate
    ) -> Category | None:
        return self.repo.update(category_id, data)

    def delete_category(self, category_id: int) -> Category | None:
        return self.repo.delete_by_id(category_id)