# Заполнить словарь, где ключами будут выступать числа от 1 до n,
# а значениями вложенный словарь с ключами 'name' и 'email', значения для ключей - с клавиатуры
n = int(input('Write n: '))
data = {
    i: dict(name=input('Write your name '), email=input('Write your email '))
    for i in range(1, n + 1)}
print(data)
