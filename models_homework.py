from sqlalchemy import Column, INT, VARCHAR, ForeignKey, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

class Base(DeclarativeBase):

    id = Column(INT, primary_key=True)
    engine = create_engine('postgresql://julia:julia@localhost:5432/db_0602')
    _Session = sessionmaker(bind=engine)

class Role(Base):
    __tablename__ = 'roles'

    name = Column(VARCHAR(15), nullable=False)
class Category(Base):
    __tablename__ = 'categories'

    name = Column(VARCHAR(255), nullable=False)
class User(Base):
    __tablename__ = 'users'

    username = Column(VARCHAR(255), nullable=False)
    email = Column(VARCHAR(255), nullable=False)
    role_id = Column(INT, ForeignKey('roles.id', ondelete='CASCADE'), nullable=False)

class Comment(Base):
    __tablename__ = 'comments'

    user_id = Column(INT, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    topic_id = Column(INT, ForeignKey('topics.id', ondelete='CASCADE'), nullable=False)
    parent_id = Column(INT, ForeignKey('comments.id', ondelete='CASCADE'), nullable=False)


class Topic(Base):
    __tablename__ = 'topics'

    author_id = Column(INT, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    category_id = Column(INT, ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)





