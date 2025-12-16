from product_utils import Product, Store

store = Store()

p1 = Product(1, "Laptop", 1000, 2)
p2 = Product(2, "Mouse", 50, 5)
p3 = Product(1, "Laptop", 1000, 1)

store.add_product(p1)
store.add_product(p2)
store.add_product(p3)

store.list_products()
print("Total value:", store.total_value())
