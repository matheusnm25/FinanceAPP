from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.company import CompanyService
from app.schemas.company import CompanyCreate, CompanyUpdate, CompanyResponse
from app.database import get_db

router = APIRouter(prefix="/companies", tags=["Companies"])

@router.post("/", response_model=CompanyResponse)
def create_company(
    data: CompanyCreate,
    db: Session = Depends(get_db)
):
    return CompanyService(db).create_company(data)


@router.get("/{company_id}", response_model=CompanyResponse)
def get_company(
    company_id: int,
    db: Session = Depends(get_db)
):
    company = CompanyService(db).get_company(company_id)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    return company


@router.get("/", response_model=list[CompanyResponse])
def list_companies(
    db: Session = Depends(get_db)
):
    return CompanyService(db).list_companies()


@router.put("/{company_id}", response_model=CompanyResponse)
def update_company(
    company_id: int,
    data: CompanyUpdate,
    db: Session = Depends(get_db)
):
    company = CompanyService(db).update_company(company_id, data)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    return company


@router.delete("/{company_id}", response_model=CompanyResponse)
def delete_company(
    company_id: int,
    db: Session = Depends(get_db)
):
    company = CompanyService(db).delete_company(company_id)
    if not company:
        raise HTTPException(status_code=404, detail="Company not found")
    return company