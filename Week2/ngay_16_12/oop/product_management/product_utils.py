class Product:
    def __init__(self, product_id, name, price, quantity):
        self.id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"


class Store:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        for p in self.products:
            if p.id == product.id:
                p.quantity += product.quantity
                return
        self.products.append(product)

    def remove_product(self, product_id):
        self.products = [p for p in self.products if p.id != product_id]

    def list_products(self):
        if not self.products:
            print("Store is empty.")
        for p in self.products:
            print(p)

    def total_value(self):
        return sum(p.price * p.quantity for p in self.products)
