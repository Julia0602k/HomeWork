# 2. Написать класс Rectangle
# Конструктор класса принимает координаты точек по диагонали (правая нижняя, верхняя
# левая или левая нижняя, правая верхняя)
# Написать метод perimeter возвращающий периметр получившегося прямоугольника
# Написать метод square возвращающий площадь получившегося прямоугольникаы
# *учесть, что координаты на плоскости могут быть отрицательными

class Rectangle():
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def perimeter(self):
        perimeter_rectangle = abs(self.x2 - self.x1)*2 + abs(self.y2 - self.y1)*2
        return perimeter_rectangle
    def square(self):
        square_rectangle = abs(self.x2 - self.x1)*abs(self.y2 - self.y1)
        return square_rectangle
    def __str__ (self):
        return f'Периметр прямоугольника равен {self.perimeter()} см, площадь прямоугольника равен {self.square()} см2'
ex_1 = Rectangle(1, 1, 3, 5)
ex_2 = Rectangle(1, -1, -3, 8)
print(ex_1)
print(ex_2)
