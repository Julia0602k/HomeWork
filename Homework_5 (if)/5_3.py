#вывести четные числа от 2 до N по 5 в строкe
N = int(input('Введите N: '))
count = 0
for i in range(2, N+1):
    if i % 2 == 0:
        print(i, end=' ')
        count += 1
    if count == 5:
        print('\n')
        count = 0