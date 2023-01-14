# Пользователь вводит 3 числа, найти среднее арифмитическое с точностью 3
print('Write three numbers')
number1 = float(input('First:'))
number2 = float(input('Second:'))
number3 = float(input('Third:'))
summa = number1 + number2 + number3
arithmetic_mean = summa / 3
print(round(arithmetic_mean, 3))