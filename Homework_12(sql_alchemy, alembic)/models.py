from sqlalchemy import Column, TIMESTAMP, INTEGER, SMALLINT, INT, \
    VARCHAR, BOOLEAN, ForeignKey, DECIMAL, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from datetime import datetime

class Base(DeclarativeBase):

    id = Column(INT, primary_key=True)
    engine = create_engine('sqlite:///alchemy.sqlite3')
    _Session = sessionmaker
class Category(Base):
    __tablename__ = 'categories'

    name = Column(VARCHAR(64), unique=True, nullable=False)
    is_published = Column(BOOLEAN, default=True)

class Product(Base):
    __tablename__ = 'products'

    name = Column(VARCHAR(64), nullable=False)
    descr = Column(VARCHAR(1024), nullable=True)
    price = Column(DECIMAL(8, 2),  nullable=False)
    is_published = Column(BOOLEAN, default=True)
    category_id = Column(INT, ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)

class Status(Base):
    __tablename__ = 'statuses'

    id = Column(SMALLINT, primary_key=True)
    name = Column(VARCHAR(15), unique=True, nullable=True)


class User(Base):
    __tablename__ = 'users'

    username = Column(VARCHAR(128), nullable=True)
    # name = Column(VARCHAR(15), unique=True, nullable=True)

class Order(Base):
    __tablename__ = 'orders'

    status_id = Column(SMALLINT, ForeignKey('statuses.id', ondelete='RESTRICT'), nullable=False)
    user_id = Column(INT, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    date_created = Column(TIMESTAMP, default=datetime.utcnow)

class OrderItem(Base):
    __tablename__ = 'order_items'

    order_id = Column(SMALLINT, ForeignKey('orders.id', ondelete='CASCADE'), nullable=False)
    product_id = Column(INT, ForeignKey('products.id', ondelete='CASCADE'), nullable=False)



# Base.metadata.create_all(bind=Base.engine)
# Base.metadata.drop_all(bind=Base.engine)

