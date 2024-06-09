from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class UserType(Base):
  __tablename__ = "user_types"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, unique=True, index=True)
  
  
  users = relationship("User", back_populates="user_type")