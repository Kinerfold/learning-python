class Inventory:
    
    inventory = {
        "Keyboard": 10,
        "Mouse": 25,
        "Monitor": 5
    }
    
    def __init__(self):
        pass
        
    def add_product(self, name, quantity):
        if name not in self.inventory:
            self.inventory[name] = quantity
            print('Товар не найден!')
        else: 
            print('Товар добавлен!')
        
    def show_products(self):
        for key, value in self.inventory.items():
            print(f"{key}: {value}")

    def find_product(self, name):
        if name not in self.inventory:
                print('Товар не найден!')
        else: 
                print(f"Найден товар: {name}") 
        
    def delete_product(self, name):
        if name not in self.inventory:
             del self.inventory(name)
             print('Товар не найден!')
        else:
            del self.inventory[name]
            
    def update_quantity(self, name):
        if name not in self.inventory:
            print('Товар не найден!')
        else:
            new_quantity = int(input("Введите количество: "))
            self.inventory[name] = new_quantity
    
    def checking_quantity(self, name):
        new_quantity = int(input("Введите количество: "))
        if new_quantity > 0:
            self.inventory[name] = new_quantity
            print(f'Количество изменено!')
        else:
            print('Неверное количество!')