from sqlalchemy import ForeignKey, Integer, String, Table, Column
from config import Base

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    email = Column(String, index=True, unique=True)
    designation = Column(Integer, ForeignKey("designations.id"))

class Designations(Base):
    __tablename__ = 'designations'

    id = Column(Integer, primary_key=True)
    designation_text = Column(String, index=True)
    salary = Column(Integer)

