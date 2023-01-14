# Пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами
text = input('Write a sentence:')
sentence1 = text.replace(' ', '-')
print(sentence1)

sentence2 = text.split(' ')
sentence2 = '-'.join(sentence2)
print(sentence2)