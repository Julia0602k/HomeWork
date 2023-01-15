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
            sum += i
        return sum/len(self.numbers)
    def max_count(self):
        dict1 = {}
        for i in self.numbers:
            if i not in dict1.values():
                dict1[i] = 1
            else:
                dict1[i] += 1
        list2 = sorted(dict1.items(), key=lambda i: i[1], reverse=True)
        list_max_count = []
        max_count = 0
        for tup in list2:
            if tup[1] >=



        # dict1.clear()
        # for i in list2:
        #     dict1[i[0]] = i[1]
        # return list2, dict1
        # dict1 = dict(list2)
        # return dict1, dict2
        # for i in list2:
        #     count = 0
        #     if i


    def __str__(self):
        return f'''Среднее арифметическое среди всех чисел: {self.average()}'''
list1 = Numbers([1, 2, 3, 4, 5, 1, 2, 3, 1, 2, 3, 3, 3, 3])
# print(list1)
print(list1.max_count())
