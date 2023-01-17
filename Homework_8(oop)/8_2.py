# 2. Написать класс Taxi
# Конструктор класса принимает атрибуты: cars: list[Car] (список экземпляров класса Car)
# 2.1 Реализовать метод find_car
# На вход метода поступают атрибуты: count_passengers, is_baby (количество пассажиров,
# наличие ребенка, примечание: количество пассажиров с учетом ребенка если он есть)
# На основании данных, вернуть объект Car из атрибута cars подходящий по параметрам и
# свободный (is_busy = False), у автомобиля сменить атрибут is_busy на значение True, если
# подходящего автомобиля нет, метод должен возвращать None

class Car:
    def __init__(self, color: str, count_passenger_seats: int, is_baby_seat: bool):
        self.color = color
        self.count_passenger_seats = count_passenger_seats
        self.is_baby_seat = is_baby_seat
        self.is_busy = False

    def __str__(self):
        return f'''Автомобиль: цвет {self.color}, количество пассажирских мест: {self.count_passenger_seats}, 
наличие десткого кресла: {'Есть' if self.is_baby_seat else 'Нет'}'''
    def make_busy(self):
        if self.is_busy == False:
            self.is_busy = True
        else:
            self.is_busy = False
class Taxi:
    def __init__(self, cars: list):
        self.cars = cars
    def find_car(self, count_passengers, is_baby):
        for car in self.cars:
            if count_passengers <= car.count_passenger_seats and car.is_busy is False:
                if is_baby and car.is_baby_seat or not is_baby:
                    car.make_busy()
                    print(car)
                    break
        else:
            return None

car1 = Car('красный', 3, True)
car2 = Car('желтый', 2, False)
car3 = Car('зеленый', 4, True)
car4 = Car('синий', 3, False)
car5 = Car('фиолетовый', 5, True)
cars = Taxi([car1, car2, car3, car4, car5])

count_passengers = int(input('Введите требуемое количество мест: '))
is_baby = input('Если требуется детское автокресло, введите цифру 1; есть нет, введите 0. Сделайте выбор: ')
cars.find_car(count_passengers, is_baby)
