from jose import jwt
from datetime import datetime, timedelta
from os import getenv
from sqlalchemy.orm import Session
from schemas.user_schema import User
from views.user.users_view import get_user_by_email
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import bcrypt
from fastapi import Depends, HTTPException, status

security = HTTPBearer()

def generate_token(expiration_minutes: int, user: User) -> str:
    expiration_time = datetime.utcnow() + timedelta(minutes=expiration_minutes)
    payload = {
        "exp": expiration_time,
    }
    payload.update(user.dict())
    token = jwt.encode(payload, getenv("SECRET_KEY_TOKEN"), algorithm='HS256')
    return token
  
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
  
def validate_credentials(email: str, password: str, db: Session) -> bool:
    user = get_user_by_email(email, db)
    if user:
      if user.hashed_password is None:
          return False
      elif verify_password(password, user.hashed_password):
        return generate_token(9999999, User(**user.__dict__))
    else:
      return False    
    
async def validate_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        if credentials.scheme != "Bearer":
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Esquema de autenticación incorrecto")
        if not verify_token(token):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")
    except IndexError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token no proporcionado")


def verify_token(token: str) -> bool:
    try:
        payload = jwt.decode(token, getenv("SECRET_KEY_TOKEN"), algorithms=["HS256"])

        expiration_time = datetime.fromtimestamp(payload["exp"])
        if expiration_time < datetime.utcnow():
            raise HTTPException(status_code=401, detail="Token expired")
        return True
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")