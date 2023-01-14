#вывести первые N чисел, кратные M и больше K

n = int(input('Write n: '))
m = int(input('Write m: '))
k = int(input('Write k: '))
count = 0
a = 0
while count < n:
    a += 1
    if a % m == 0 and a > k:
        print(a, end=' ')
        count += 1

