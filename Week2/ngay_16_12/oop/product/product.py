class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def tinh_tong(self):
        return self.price * self.quantity

    def info_product(self):
        print("Tên hàng: ", self.name)
        print("Giá: ", self.price)
        print("Số lượng: ", self.quantity)
        print("Tổng tiền: ", self.tinh_tong())