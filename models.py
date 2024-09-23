from sqlalchemy import String, Column, Integer, DateTime
from database import engine, Base

class Event(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    description = Column(String(100))
    date = Column(String(50))
    location = Column(String(50))
    category = Column(String(50))
    media  = Column(String(50))


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(50))
    name = Column(String(50))
    email = Column(String(50))
    telephone = Column(String(50))
    