from sqlalchemy import select, or_, and_
from sqlalchemy.orm import Session, sessionmaker

from models import Category

cat = Category.get(1)
print(cat.name)

# with Category._Session() as session:
#     # session: Session
#     cat = Category(name='Fruits', is_published=1)
#     session.add(cat)
#     session.commit()
    # session.refresh(cat)
    # print(cat.id)
    # print(cat.name)
    # print(cat.is_published)
    # query = session.scalars(
    #     select(Category)
    #     .order_by('name')
    # )
    # categories = query.all()
    # print(categories[0].name)

    # for category in query.all():
        # category.name = 'Food'

    # category = session.get(Category, 1)

