from sqlalchemy import Column, INTEGER, INT, VARCHAR, BOOLEAN, ForeignKey, DECIMAL
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):

    id = Column(INT, primary_key=True)

class Category(Base):
    __tablename__ = 'categories'

    name = Column(VARCHAR(64), unique=True, nullable=False)
    is_published = Column(BOOLEAN, default=True)

class Product(Base):
    __tablename__ = 'products'

    name = Column(VARCHAR(64), unique=True, nullable=False)
    descr = Column(VARCHAR(1024), unique=True, nullable=False)
    price = Column(DECIMAL(8, 2), unique=True, default=1.0)
    is_published = Column(BOOLEAN, default=True)
    category_id = Column()