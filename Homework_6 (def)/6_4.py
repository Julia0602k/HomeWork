#Дан список, содержащий в себе различные типы данных, отфильтровать таким образом,
# чтобы остались только строки, без использования доп.списка
list1 = [12, True, 'hello', 111, 15.1, 'python']
list1 = list(filter(lambda i: isinstance(i, str), list1))
print(list1)

