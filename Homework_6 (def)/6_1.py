#Написать функцию перевода десятичного числа в двоичное и обратно, без использования функции int
number1 = int(input('Write a decimal number: '))
def decimal_number_to_bin(number1) -> str:
    binary = ''
    while number1 > 1:
        binary += str(number1 % 2)
        number1 //= 2
    binary += str(number1)
    return binary[::-1]

print(decimal_number_to_bin(number1))

binary1 = decimal_number_to_bin(number1)
def bin_number_to_decimal(binary1: str) -> int:
    number2 = 0
    for i in binary1:
        number2 *= 2
        number2 += int(i)
    return number2

print(bin_number_to_decimal(binary1))
