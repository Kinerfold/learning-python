class Product:
    
    def __init__(self, name, price, quantity, inventory):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.inventory = {
    "Keyboard": 10,
    "Mouse": 25,
    "Monitor": 5
}
        
        def add_product(self):
            if inventory == "Keyboard":
                inventory.append(int)
                print('Товар добавлен!')
                
            if inventory == "Mouse":
                inventory.append(int)
                print('Товар добавлен!')
            
            if inventory == "Monitor":
                inventory.append(int)
                print('Товар добавлен!')
            else:
                return 'Товара не существует!'
        
        def show_products(self):
            return inventory
        
        def find_product(self):
            if name:
               print(f"Найден товар: {name}, Цена: {price}, Колво: {quantity}")
            else:
                print('Товар не найден')
        
        def delete_product(self):
             if inventory == 'Monitor':
                 inventory.remove('Monitor')
             
             if inventory == 'Mouse':
                 inventory.remove('Mouse')
             
             if inventory == 'Keyboard':
                 inventory.remove('Keyboard')
             else:
                 return 'Товара нет!'
            
        def update_quantity(self):
            if inventory == 'Mouse':
                inventory.append(int)
            
            if inventory == 'Keyboard':
                inventory.append(int)
            
            if inventory == 'Keyboard':
                inventory.append(int)
    
class Inventory(Product):
    
    products = []
    pass
