from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.user import UserService
from app.schemas.user import UserCreate, UserUpdate, UserResponse
from app.database import get_db

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponse)
def create_user(
    data: UserCreate,
    db: Session = Depends(get_db),
):
    try:
        return UserService(db).create_user(data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{user_id}", response_model=UserResponse)
def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    user = UserService(db).get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int,
    data: UserUpdate,
    db: Session = Depends(get_db)
):
    user = UserService(db).update_user(user_id, data)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.delete("/{user_id}", response_model=UserResponse)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    user = UserService(db).delete_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user