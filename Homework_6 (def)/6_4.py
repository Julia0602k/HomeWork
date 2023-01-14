#Дан список, содержащий в себе различные типы данных, отфильтровать таким образом,
# чтобы остались только строки, без использования доп.списка
list1 = [12, True, 'hello', 111, 15.1, 'python']
list1 = list(filter(lambda i: isinstance(i, str), list1))
print(list1)

# def func111(list1):
#     for i in range(len(list1)-1, -1, -1):
#         if not isinstance(list1[i], str):
#             del list1[i]
#     return list1
# print(func111(list1))

