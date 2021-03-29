from sqlalchemy import Column, Boolean, Integer, String, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    # username = Column(String)
    # create_time = Column(String,nullable=False)
    # loginTime = Column(String,nullable=False)
    hashed_password = Column(String, nullable=True)
    is_active = Column(Boolean, nullable=True)
    # is_superuser = Column(Boolean, nullable=True)

    items = relationship('Item', back_populates='owner')


class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
