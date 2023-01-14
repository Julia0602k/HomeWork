#Дан список рандомных чисел, необходимо его отсортировать: сначала четные, потом нечетные
numbers1 = [1, 2, 6, 5, 9]

def filter_even_odd(numbers1):
    list_answer = list(filter(lambda x: x % 2 == 0, numbers1))
    list_odd = list(filter(lambda x: x % 2, numbers1))
    list_answer.extend(list_odd)
    print(list_answer)

filter_even_odd(numbers1)

