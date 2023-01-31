from models import Category
# from sqlalchemy import select, or_, and_

# with Category._Session() as session:
#     session: Session
    # cat = Category(name='Fruits')
    # session.add(cat)
    # session.commit()
    # session.refresh(cat)
    # print(cat.id)
    # print(cat.name)
    # print(cat.is_published)
    # query = session.scalars(
    #     select(Category)
    #     .filter(Category.id > 0)
    #     .filter(Category.is_published.)
    #     # .where()

    category = session.get(Category, 1)

