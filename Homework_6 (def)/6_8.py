#Дан словарь, ключ - название страны, значение - список городов,
#На вход поступает город, необходимо сказать из какой он страны
city = input('Введите город: ')
dict_city = {'Belarus': ['Minsk', 'Brest'], 'Germany': ['Berlin', 'Hamburg'], 'Great Britain': ['London', 'Liverpool', 'Manchester']}
def what_country(city, dict_city):
    for k, v in dict_city.items():
        if city in v:
            print(f'{city} is located in {k}')
what_country(city, dict_city)
