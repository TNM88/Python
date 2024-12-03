class Vehicle:
    def __init__(self, color):
        self.color = color

    def vehicleInfo(self):
        print(f"Vehicle Color: {self.color}")


class Taxi(Vehicle):
    def __init__(self, color, model, capacity, variant):
        super().__init__(color)
        self._model = model
        self._capacity = capacity
        self._variant = variant

    def getModel(self):
        return self._model

    def setModel(self, model):
        self._model = model

    def getCapacity(self):
        return self._capacity

    def setCapacity(self, capacity):
        self._capacity = capacity

   
    def getVariant(self):
        return self._variant

    def setVariant(self, variant):
        self._variant = variant

    def vehicleInfo(self):
        super().vehicleInfo()
        print(f"Model: {self._model}, Capacity: {self._capacity}, Variant: {self._variant}")


t1 = Taxi("Yellow", "Sedan", 4, "Basic")
t2 = Taxi("White", "SUV", 7, "Premium")

t1.vehicleInfo()
t2.vehicleInfo()
