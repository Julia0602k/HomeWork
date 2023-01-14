# Пользователь вводит 3 числа, сказать сколько из них положительных и сколько отрицательных
number1 = int(input('Write a first number:'))
number2 = int(input('Write a second number:'))
number3 = int(input('Write a third number:'))

summa_positive1 = (number1 > 0) + (number2 > 0) + (number3 > 0)
summa_negative1 = 3 - summa_positive1
print('Answer is:\n', '\tpositive:', summa_positive1, '\n\tnegative:', summa_negative1)
