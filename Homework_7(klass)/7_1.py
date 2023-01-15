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
def student_sort(students: list[Student]):
    return students.sort()

students = [Student('Василий', 231, [5, 8, 7]), Student('Мария', 156, [1, 8, 3, 7]), Student('Евгений', 568, [9, 8, 9, 9, 9])]
vasya = Student('Василий', 231, [5, 8, 7])
print(vasya)
print(students)
