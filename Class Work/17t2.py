from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand

    @abstractmethod
    def start_engine(self):
        pass

    def description(self):
        return f"This is a vehicle of brand {self.brand}."

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def start_engine(self):
        print(f"The engine of the {self.brand} {self.model} is starting.")

    def description(self):
        return f"This is a {self.brand} car, model {self.model}."

if __name__ == "__main__":
    my_car = Car("Toyota", "Corolla")
    print(my_car.description())
    my_car.start_engine()

    try:
        my_vehicle = Vehicle("GenericBrand")
    except TypeError as e:
        print(f"Error: {e}")
