from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.group import GroupService
from app.schemas.group import GroupCreate, GroupUpdate, GroupResponse
from app.database import get_db

router = APIRouter(prefix="/groups", tags=["Groups"])

@router.post("/", response_model=GroupResponse)
def create_group(
    data: GroupCreate,
    db: Session = Depends(get_db)
):
    return GroupService(db).create_group(data)


@router.get("/{group_id}", response_model=GroupResponse)
def get_group(
    group_id: int,
    db: Session = Depends(get_db)
):
    group = GroupService(db).get_group(group_id)
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    return group


@router.get("/company/{company_id}", response_model=list[GroupResponse])
def list_groups_by_company(
    company_id: int,
    db: Session = Depends(get_db)
):
    return GroupService(db).list_groups_by_company(company_id)


@router.put("/{group_id}", response_model=GroupResponse)
def update_group(
    group_id: int,
    data: GroupUpdate,
    db: Session = Depends(get_db)
):
    group = GroupService(db).update_group(group_id, data)
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    return group


@router.delete("/{group_id}", response_model=GroupResponse)
def delete_group(
    group_id: int,
    db: Session = Depends(get_db)
):
    group = GroupService(db).delete_group(group_id)
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    return group