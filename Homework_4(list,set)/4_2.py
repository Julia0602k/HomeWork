# Написать программу, которая будет создавать словарь для подсчитывания
# количества вхождений каждой буквы в текст, введенный с клавиатуры
text1 = input('Write a text: ')
dict1 = {}
for i in text1:
    if i not in dict1.values():
        count1 = text1.count(i)
        dict1[i] = count1
print(dict1)
