#Дан словарь словарей, ключ внешнего словаря - id пеользователя,
# значение - словарь с данными о пользователе (имя, фамилия, телефон, почта),
# вывести имена тех, у кого не указана почта (нет ключа email или значение этого ключа пустая строка)
data1 = {111: {'name': 'Vasya', 'surname': 'Ivanov', 'phone_number': '+3752955566777', 'email': ''},
         222: {'name': 'Masha', 'surname': 'Zhukova', 'phone_number': '+375291234567', 'email': '123@mail.ru'},
         333: {'name': 'Sveta', 'surname': 'Mashkova', 'phone_number': '+375291258964', 'email': ''},
         444: {'name': 'Dasha', 'surname': 'Petrova', 'phone_number': '+375298945612', 'email': 'lll22@tut.by'},
         }
def no_email(data1):
    print("There are users, who don't have email:")
    for key, value in data1.items():
        for k, v in value.items():
            if k == 'email' and v == '':
                print(value['name'])
no_email(data1)