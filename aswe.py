class Human:
    def __init__(self, name):
        self.name = name

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passengers(self, *args):
        for passenger in args:
            self.passengers.append(passenger)

    def print_passengers_names(self):
        if self.passengers:
            print(f"В автомобілі {self.brand} є такі пасажири:")
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print(f"У автомобілі {self.brand} немає пасажирів!")

h1 = Human(input("Введіть ім'я першої людини: "))
h2 = Human("Vetal")

car1 = Auto("Mercedes")
car1.add_passengers(h1, h2)
car1.print_passengers_names()
