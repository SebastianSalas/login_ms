from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from views.auth.auth_view import validate_credentials
from models.user_model import User as UserModel
from schemas.user_schema import User, UserCreate

auth_router = APIRouter()

@auth_router.post("/login")
async def login(credentials: dict, db: Session = Depends(get_db)):
    email = credentials.get("email")
    password = credentials.get("password")
    
    token = validate_credentials(email, password, db)
    return {"message": token}

@auth_router.post("/logout")
async def logout():
    return {"message": "Logout Successful"}