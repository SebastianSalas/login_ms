from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from .user_type_model import UserType
from .document_type_model import DocumentType

class User(Base):
  __tablename__ = "users"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, nullable=True)
  last_name = Column(String, nullable=True)
  email = Column(String, nullable=True)
  document_type_id = Column(Integer, ForeignKey("document_types.id"))
  phone_number = Column(String, nullable=True)
  document = Column(String, unique=True, index=True)
  user_type_id = Column(Integer, ForeignKey('user_types.id'))
  hashed_password = Column(String)
  
  
  user_type = relationship("UserType", back_populates="users")
  document_type = relationship("DocumentType", back_populates="users")