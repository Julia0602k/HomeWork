#На вход поступает простейшая химическая формула C2H5OH.
# Вернуть словарь вида {назв атома: количество}. Ответ {'C': 2, 'H': 6, 'O': 1}
formula = 'C2H5OH'
def count_formula(formula: str):
    dict1 = {}
    for i in formula:
        if i.isalpha():
            dict1.setdefault(i, formula[formula.index(i)+1])

    return dict1
print(count_formula(formula))