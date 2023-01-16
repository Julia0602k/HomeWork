# 3. Написать класс Numbers
# Конструктор класса принимает список чисел numbers: list[int]
# Написать метод average — возвращающий среднее арифметическое между всеми числами
# Написать метод max_count — возвращающий число из списка, которое чаще встречается,
# если таких чисел несколько, вывести среднее арифметическое среди таких чисел
class Numbers():
    def __init__(self, numbers: list[int]):
        self.numbers = numbers

    def average(self):
        return sum(self.numbers)/len(self.numbers)

    def __str__(self):
        return f'''Среднее арифметическое среди всех чисел: {self.average()}'''

list1 = Numbers([1, 2, 3, 4, 5, 1, 2, 3, 1, 2, 3, 3, 3, 3])
print(list1.average())
# print(list1)
# print(list1.max_count())
