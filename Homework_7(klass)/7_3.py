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
            if i not in dict1.keys():
                dict1[i] = 1
            else:
                dict1[i] += 1
        max_amount = 0
        c = 0
        this_number = 0
        for k, v in dict1.items():
            if v > max_amount:
                max_amount = v
                this_number =
                c = 0
            elif v == max_amount:

                c += 1
        if c == 0:
            return f'Число, которое чаще встречается {max_count}'
        else:
            return f'Среднее арифметическое среди наиболее часто встречающихся чисел: {m}'



        # list2 = sorted(dict1.items(), key=lambda i: i[1], reverse=True)

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
