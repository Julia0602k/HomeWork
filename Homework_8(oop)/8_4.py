# 4. Изменить класс выше, список категорий должен содержать не просто имена категорий, а
# словари с данными о каждой категории (name: str, is_published: bool), а так же изменить
# методы add, get, delete, update для работы с списком словарей
# 4.1 Добавить метод make_published принимающий индекс категории и меняющий значение
# ключа is_published на True, если такого индекса нет, вызвать исключение IndexError
# 4.2 Добавить метод make_unpublished принимающий индекс категории и меняющий
# значение ключа is_published на False, если такого индекса нет, вызвать исключение
# IndexError
class Category:
    categories: list[dict[str:str, str: bool]]
    categories = []
    @classmethod
    def add(cls, category: str):
        for i in cls.categories:
            if category in i.values:
                raise ValueError
        else:
            return cls.categories.append({'name': category, 'is_published': False})

    @classmethod
    def get(cls, index: int):
        if index in range(len(cls.categories)):
            return cls.categories[index]['name']
        raise IndexError

    @classmethod
    def delete(cls, index: int) -> None:
        if index in range(len(cls.categories)):
            del cls.categories[index]

    @classmethod
    def update(cls, index, category):
        if index not in range(len(cls.categories)):
            for i in cls.categories:
                if category in i.values:
                    raise ValueError
            else:
                return cls.categories.append({'name': category, 'is_published': False})

    @classmethod
    def make_published(cls, index: int):
        if index in range(len(cls.categories)):
            cls.categories[index]['is_published'] = True
        raise IndexError

    @classmethod
    def make_unpublished(cls,  index: int):
        if index in range(len(cls.categories)):
            cls.categories[index]['is_published'] = False
        raise IndexError


