
class Vehicle:
    def __init__(self, brand, wheels):
        self.brand = brand
        self.wheels = wheels

    def display(self):
        print(f"Brand: {self.brand}")
        print(f"Wheels: {self.wheels}")


class Car(Vehicle):
    def __init__(self, brand, wheels, model):
        super().__init__(brand, wheels)
        self.model = model

    
    def display(self):
        super().display()
        print(f"Model: {self.model}")



car = Car("Toyota", 4, "Corolla")
car.display()


print(issubclass(Car, Vehicle))
