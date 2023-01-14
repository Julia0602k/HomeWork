#Дан список чисел и на вход поступает число N, необходимо сместить список на указанное число,
# #пример [1,2,3,4,5,6,7], N=3, ответ [5,6,7,1,2,3,4]
number1 = int(input('Write number N: '))
list1 = [1, 2, 3, 4, 5, 6, 7]
def move_index(list1, number1):
    list2 = list1[-number1:]
    list2.extend(list1[:-number1])
    print(list2)
move_index(list1, number1)
