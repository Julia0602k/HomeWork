# 3. Реализовать класс Category
# Создать атрибут класса categories
# 3.1 Написать метод класса add принимающий на вход название категории, если такой
# категории в атрибуте класса categories нет, добавить данную категорию в список и вернуть
# индекс вхождения новой категории в списке. Если такая категория уже есть, вызвать
# исключение ValueError
# 3.2 Написать метод класса get принимающий индекс и возвращающий категорию из списка
# категорий на этом индексе, если нет элемента на таком индексе, вызвать исключение
# IndexError
# 3.3 Написать метод класса delete принимающий индекс категории в списке категорий и
# удаляющий элемент из списка категорий на этом индексе, если нет элемента на таком
# индексе, ничего не делать, метод ничего возвращать не должен
# 3.4 Написать метод класса update принимающий индекс категорий и новое название
# категории, если нет элемента на таком индексе, то новая категория должна добавляться с
# учетом того, что имена категорий уникальны, если новое имя категории нарушает
# уникальность в списке категорий, вызвать исключение ValueError
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

