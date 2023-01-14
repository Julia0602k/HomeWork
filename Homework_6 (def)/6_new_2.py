# 2. На вход функции поступает список словарей humans и gender (m/w), каждый словарь
# содержит ключи: gender(пол), height(рост) людей, вернуть средний рост людей
# указанного пола
humans = [
    {'gender': 'w', 'height': 168},
    {'gender': 'm', 'height': 178},
    {'gender': 'w', 'height': 161},
    {'gender': 'm', 'height': 185},
    {'gender': 'w', 'height': 175},
    {'gender': 'm', 'height': 181},
    {'gender': 'w', 'height': 167},
    {'gender': 'm', 'height': 193}
    ]
def average_height(humans: list[dict[str, str]]):
    height_m = 0
    count_m = 0
    height_w = 0
    count_w = 0
    for i in humans:
        if 'm' in i.values():
            height_m += i.get('height')
            count_m += 1
        else:
            height_w += i.get('height')
            count_w += 1
    return f'Средний рост мужчин {height_m/count_m} см, Средний рост женщин {height_w/count_w} см'
print(average_height(humans))




