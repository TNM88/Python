class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_detail(self):
        print(f"Name: {self.name}, Price: {self.price}")


class ElectronicProduct(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty

    def display_detail(self):
        super().display_detail()
        print(f"Warranty: {self.warranty}")
product = Product("Generic Product", 100)
product.display_detail()

electronic_product = ElectronicProduct("Smartphone", 500, "2 years")
electronic_product.display_detail()
