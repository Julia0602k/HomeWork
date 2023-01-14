# заполнить список степенями числа 2 (от 2^1 до 2^n)
n = int(input('Введите n: '))
list1 = []
for i in range(1, n + 1):
    list1.append(2 ** i)
print(list1)
