class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
        def add_product(self):
            return "Товар успешно добавлен."

        def show_products(self):
            return f"{name}, Цена: {price}, Колво: {quantity}"
        
        def find_product(self):
            if name:
               print(f"Найден товар: {name}, Цена: {price}, Колво: {quantity}")
            else:
                print('Товар не найден')
        
        def delete_product(self):
             return __dict__.clear(name)
             print('Товар удалён')
            
        def update_quantity(self):
            pass
    
class Inventory(Product):
    
    products = []
    pass
