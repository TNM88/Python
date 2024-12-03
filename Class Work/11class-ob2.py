class Shape:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def display(self):
        print(f"Shape: {self._name}")

    def display_info(self):
        print("Shape details")


class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self._length = length
        self._width = width

    def area(self):
        return self._length * self._width

    def perimeter(self):
        return 2 * (self._length + self._width)
shape = Shape("Generic Shape")
shape.display()
shape.display_info()

rectangle = Rectangle("Rectangle", 10, 5)
rectangle.display()
print(f"Area: {rectangle.area()}")
print(f"Perimeter: {rectangle.perimeter()}")
