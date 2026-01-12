from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.category import CategoryService
from app.schemas.category import CategoryCreate, CategoryUpdate, CategoryResponse
from app.database import get_db

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.post("/", response_model=CategoryResponse)
def create_category(
    data: CategoryCreate,
    db: Session = Depends(get_db)
):
    return CategoryService(db).create_category(data)


@router.get("/{category_id}", response_model=CategoryResponse)
def get_category(
    category_id: int,
    db: Session = Depends(get_db)
):
    category = CategoryService(db).get_category(category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@router.get("/company/{company_id}", response_model=list[CategoryResponse])
def list_categories_by_company(
    company_id: int,
    db: Session = Depends(get_db)
):
    return CategoryService(db).list_categories_by_company(company_id)


@router.put("/{category_id}", response_model=CategoryResponse)
def update_category(
    category_id: int,
    data: CategoryUpdate,
    db: Session = Depends(get_db)
):
    category = CategoryService(db).update_category(category_id, data)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@router.delete("/{category_id}", response_model=CategoryResponse)
def delete_category(
    category_id: int,
    db: Session = Depends(get_db)
):
    category = CategoryService(db).delete_category(category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category