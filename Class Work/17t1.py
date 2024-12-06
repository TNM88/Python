from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        print("The car is starting.")

    def stop(self):
        print("The car is stopping.")

class Motorcycle(Vehicle):
    def start(self):
        print("The motorcycle is starting.")

    def stop(self):
        print("The motorcycle is stopping.")

if __name__ == "__main__":
    my_car = Car()
    my_motorcycle = Motorcycle()

    my_car.start()
    my_car.stop()

    my_motorcycle.start()
    my_motorcycle.stop()
