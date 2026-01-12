from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.permission import PermissionService
from app.schemas.permission import (
    PermissionCreate,
    PermissionUpdate,
    PermissionResponse
)
from app.database import get_db

router = APIRouter(prefix="/permissions", tags=["Permissions"])

@router.post("/", response_model=PermissionResponse)
def create_permission(
    data: PermissionCreate,
    db: Session = Depends(get_db)
):
    return PermissionService(db).create_permission(data)


@router.get("/", response_model=list[PermissionResponse])
def list_permissions(
    db: Session = Depends(get_db)
):
    return PermissionService(db).list_permissions()


@router.put("/{permission_id}", response_model=PermissionResponse)
def update_permission(
    permission_id: int,
    data: PermissionUpdate,
    db: Session = Depends(get_db)
):
    permission = PermissionService(db).update_permission(permission_id, data)
    if not permission:
        raise HTTPException(status_code=404, detail="Permission not found")
    return permission


@router.delete("/{permission_id}", response_model=PermissionResponse)
def delete_permission(
    permission_id: int,
    db: Session = Depends(get_db)
):
    permission = PermissionService(db).delete_permission(permission_id)
    if not permission:
        raise HTTPException(status_code=404, detail="Permission not found")
    return permission