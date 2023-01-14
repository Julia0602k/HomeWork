# 3. На вход функции поступает список словарей users, каждый словарь содержит ключи:
# id, name, referrer_id, id у каждого пользователя уникальный, referrer_id содержит id
# пользователя, кто пригласил данного пользователя и может быть пустым,
# посчитать для каждого пользователя, каждому пользователю добавить ключ referrals_count с
# количеством человек, которых он пригласил
users = [
    {'id': 11111, 'name': 'Vasya', 'referrer_id': ''},
    {'id': 21111, 'name': 'Masha', 'referrer_id': 11111},
    {'id': 31111, 'name': 'Kate', 'referrer_id': ''},
    {'id': 41111, 'name': 'Lena', 'referrer_id': 31111},
    {'id': 51111, 'name': 'Kostya', 'referrer_id': 41111},
    {'id': 61111, 'name': 'Vera', 'referrer_id': 41111},
    {'id': 71111, 'name': 'Sanya', 'referrer_id': 51111},
    {'id': 81111, 'name': 'Lera', 'referrer_id': 51111},
    {'id': 91111, 'name': 'Vasilisa', 'referrer_id': 71111}
]
def refer(users: list[dict]):
    list_ref = []
    for i in users:
        list_ref.append(i.get('referrer_id'))
    for i in users:
        i.setdefault('referrals_count', list_ref.count(i.get('id')))
    return users

print(refer(users))