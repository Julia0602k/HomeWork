#Сделать калькулятор: у пользователя спрашивают число, потом действие и второе число
number1 = int(input('Write first number: '))
sign1 = input('Write a sign: ')
number2 = int(input('Write second number: '))
if sign1 == '+':
    print(number1 + number2)
elif sign1 == '-':
    print(number1 - number2)
elif sign1 == '*':
    print(number1 * number2)
elif sign1 == '/' and number2 != 0:
    print(number1 / number2)
else:
    print('Error')