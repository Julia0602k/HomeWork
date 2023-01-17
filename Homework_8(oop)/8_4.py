# 4. Изменить класс выше, список категорий должен содержать не просто имена категорий, а
# словари с данными о каждой категории (name: str, is_published: bool), а так же изменить
# методы add, get, delete, update для работы с списком словарей
# 4.1 Добавить метод make_published принимающий индекс категории и меняющий значение
# ключа is_published на True, если такого индекса нет, вызвать исключение IndexError
# 4.2 Добавить метод make_unpublished принимающий индекс категории и меняющий
# значение ключа is_published на False, если такого индекса нет, вызвать исключение
# IndexError
class Category:
    categories = {}
    @classmethod
    def add(cls, category: str):
        return cls.categories.setdefault(category, False)

    @classmethod
    def get(cls, category: str):
        return cls.categories.get(category)

    @classmethod
    def delete(cls, category: str) -> None:
        if category in cls.categories:
            del cls.categories[category]

    @classmethod
    def update(cls, category):
        return cls.categories.setdefault(category, False)

    @classmethod
    def make_published(cls, category):
        if category in cls.categories:
            cls.categories[category] = True
        raise IndexError

    @classmethod
    def make_unpublished(cls, category):
        if category in cls.categories:
            cls.categories[category] = False
        raise IndexError
