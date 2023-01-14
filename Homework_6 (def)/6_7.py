#Дан список чисел, необходимо для каждого элемента посчитать сумму его соседей,
# для крайних - один из соседей - число, с противоположной стороны списка
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def sum_neighbours(list1):
    for i in range(len(list1)):
        if i == 0:
            sum1 = list1[1] + list1[len(list1)-1]
        elif 1 <= i <= (len(list1)-2):
            sum1 = list1[i-1] + list1[i+1]
        else:
            sum1 = list1[0] + list1[len(list1) - 2]
        print(sum1, end=' ')
sum_neighbours(list1)
