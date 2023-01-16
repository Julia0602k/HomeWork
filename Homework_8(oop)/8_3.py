class Category():
    categories = []
    @classmethod
    def add(cls, category: str):
        if category.title() not in cls.categories:
            cls.categories.append(category.title())
            return cls.categories.index(category)
        raise ValueError

    @classmethod
    def get(cls, index: int):
        return cls.categories[index]

    @classmethod
    def delete(cls, index: int) -> None:
        if index in range(len(cls.categories)):
            del cls.categories[index]

    @classmethod
    def update(cls, index, category):
        if index not in range(len(cls.categories)):
            cls.add(category)
        elif category.title() not in cls.categories:
            cls.categories[index] = category.title()
        else:
            raise ValueError

