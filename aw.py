class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.car = None  # Початково особа не має автомобіля

    def buy_car(self, car):
        self.car = car
        print(f"{self.name} купив автомобіль {car.make} {car.model}.")

    def drive(self):
        if self.car is not None:
            print(f"{self.name} водить автомобіль {self.car.make} {self.car.model}.")
        else:
            print(f"{self.name} не має автомобіля.")

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

# Введення даних користувачем
person_name = input("Введіть ім'я особи: ")
person_age = input("Введіть вік особи: ")
car_make = input("Введіть виробника автомобіля: ")
car_model = input("Введіть модель автомобіля: ")

# Створення екземплярів особи і автомобіля
person = Person(person_name, person_age)
car = Car(car_make, car_model)

# Встановлення зв'язку між особою і автомобілем
person.buy_car(car)

# Виведення інформації про особу та автомобіль
person.drive()
