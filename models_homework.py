from sqlalchemy import Column, TIMESTAMP, INTEGER, SMALLINT, INT, \
    VARCHAR, BOOLEAN, ForeignKey, DECIMAL, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from datetime import datetime

class Base(DeclarativeBase):

    id = Column(INT, primary_key=True)
    engine = create_engine('postgresql://julia:julia@localhost:5432/db_0602')
    _Session = sessionmaker(bind=engine)

class User(Base):
    __tablename__ = 'users'

    username = Column(VARCHAR(255), nullable=False)
    email = Column(VARCHAR(255), nullable=False)
    role_id = Column(INT, ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)
    category_id = Column(INT, ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)