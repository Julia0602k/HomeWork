#Дан список чисел, надо его развернуть
# без использования reverse и функции reversed,
# а так же дополнительного списка и среза
def turning(list1: list) -> list:
    for i in range(len(list1) // 2):
        list1[i], list1[~i] = list1[~i], list1[i]
    return list1
a = [i for i in range(1,11)]
print(turning(a))
