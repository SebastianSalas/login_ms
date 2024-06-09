from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.user_model import User as UserModel
from schemas.user_schema import User, UserCreate
import bcrypt

def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(UserModel).filter(UserModel.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = hash_password(user.password) 
    db_user = UserModel(
        name=user.name,
        last_name=user.last_name,
        email=user.email,
        document=user.document,
        phone_number=user.phone_number,
        document_type_id=user.document_type_id,
        user_type_id=user.user_type_id,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
  
def all_users(db: Session = Depends(get_db)):
  return db.query(UserModel).offset(skip).limit(limit).all()

def find_user(user_id: int, db: Session = Depends(get_db)):
  return db.query(UserModel).filter(UserModel.id == user_id).first()

def get_user_by_email(email: str, db: Session = Depends(get_db)):
  return db.query(UserModel).filter(UserModel.email == email).first()
  
def get_user_by_document(document: str, db: Session = Depends(get_db)):
  return db.query(UserModel).filter(UserModel.document == document).first()

def hash_password(password: str) -> str:
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password.decode('utf-8')