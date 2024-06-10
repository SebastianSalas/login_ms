from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models.user_model import User as UserModel
from views.user.users_view import (
    create_user,
    all_users,
    find_user,
    get_user_by_document,
)
from schemas.user_schema import User, UserCreate

user_controller = APIRouter()


@user_controller.post(
    "/signup", response_model=User, status_code=status.HTTP_201_CREATED
)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_document(user.document, db)
    if db_user != None:
        raise HTTPException(status_code=400, detail="Username already registered")
    return create_user(db=db, user=user)


@user_controller.get("/users/", response_model=List[User])
def read_users(db: Session = Depends(get_db)):
    users = all_users(db)
    return users


@user_controller.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = find_user(user_id, db)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@user_controller.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_user.name = user.name
    db_user.last_name = user.last_name
    db_user.email = user.email
    db_user.document = user.document
    db_user.document_type_id = user.document_type_id
    db_user.user_type_id = user.user_type_id
    db_user.hashed_password = user.password  # Aquí deberías hashear la nueva contraseña
    db.commit()
    db.refresh(db_user)
    return db_user


@user_controller.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return {"detail": "User deleted"}
