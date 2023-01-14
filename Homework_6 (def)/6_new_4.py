# 4. Задан глобальный список products, содержащий в себе словари с данными о таварах:
# id (id товара, уникальный) title (название) price(цена) discount (скидка, диапазон значение
# от 0 до 15), на вход функции поступает список кортежей с данными о таварах,
# купленных пользователем (каждый кортеж содержит id товара и количество данного
# товара). Необходимо выпустить кассовый чек (вернуть строку), в котором будут
# указаны названия товаров, их количество, общая стоимость и общая стоимость с
# учетом скидок
products = [
    {'id': 112345, 'title': 'Телевизор', 'price': 1000, 'discount': 1},
    {'id': 212345, 'title': 'Холодильник', 'price': 1200, 'discount': 2},
    {'id': 312345, 'title': 'Принтер', 'price': 200, 'discount': 3},
    {'id': 412345, 'title': 'Ноутбук', 'price': 3300, 'discount': 4},
    {'id': 512345, 'title': 'Смартфон', 'price': 300, 'discount': 5},
    {'id': 612345, 'title': 'Кофемашина', 'price': 2000, 'discount': 6},
    ]
list_buy = [(212345, 1), (512345, 2), (612345, 1)]
def check(list_buy: list[tuple[int, int]], products: list[dict]):
    str1 = ''
    sum_all = 0
    sum_all_discount = 0
    for i in list_buy:
        for j in products:
            if i[0] in j.values():
                str1 += j.get('title') + ' - ' + str(i[1]) + ' шт., '
                sum_all += j.get('price') * i[1]
                sum_all_discount += j.get('price') * i[1] * (100 - j.get('discount'))/100
    return f'''Куплены товары: {str1}
общая стоимость товаров: {sum_all} руб,
общая стоимость товаров с учетом скидки: {sum_all_discount} руб'''
print(check(list_buy, products))