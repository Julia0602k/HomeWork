# 1. Написать класс Student
# Конструктор класса принимает аргументы: first_name: str, group: int, marks: list[int]
# Написать метод __str__ возвращающая форматированную строку с данными об студенте
# Написать функцию (не метод) student_sort принимающая список студентов: students: list[Student] и возвращающая список
# студентов отсортированный по имени

class Student():
    def __init__(self, first_name: str, group: int, marks: list[int]):
        self.first_name = first_name
        self.group = group
        self.marks = marks

    def __str__(self):
        return f'Cтудент {self.first_name} из группы N {self.group} имеет отметки {self.marks}'
def student_sort(students):
    students.sort(key=lambda x: x.first_name)
    return students


st_1 = Student('Василий', 231, [5, 8, 7])
st_2 = Student('Мария', 156, [1, 8, 3, 7])
st_3 = Student('Евгений', 568, [9, 8, 9, 9, 9])
students = [st_1, st_2, st_3]
print(st_1)
print(st_2)
print(st_3)
student_sort(students)
for st in students:
    print(st.first_name, ' ', end='')
