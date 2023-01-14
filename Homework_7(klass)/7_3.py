# 3. Написать класс Numbers
# Конструктор класса принимает список чисел numbers: list[int]
# Написать метод average — возвращающий среднее арифметическое между всеми числами
# Написать метод max_count — возвращающий число из списка, которое чаще встречается,
# если таких чисел несколько, вывести среднее арифметическое среди таких чисел
class Numbers():
    def __init__(self, numbers: list[int]):
        self.numbers = numbers

    def average(self):
        sum = 0
        for i in self.numbers:
            sum+=i
        return sum/len(self.numbers)
    def max_count(self):
        pass

    def __str__(self):
        return f'Среднее арифметическое среди всех чисел: {self.average()} \n'
list1 = Numbers([1,2,3,4,5])
# print(list1.average())
