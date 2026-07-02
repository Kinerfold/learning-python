class Inventory:
    def __init__(self, inventory):
        self.inventory = inventory
        
        inventory = {
        "Keyboard": 10,
        "Mouse": 25,
        "Monitor": 5
    }
        
    def add_product(self, name, quantity):
        if name in self.inventory:
            self.inventory[name] = quantity
            print('Товар добавлен!')
        else:
            print('Товар не найден')
        
    def show_products(self):
        for key, value in self.inventory.items():
            print(f"{key}: {value}")

    def find_product(self, name): 
        if name in self.inventory: 
            print(f"Найден товар: {name}") 
        else: 
            print('Товар не найден')
        
    def delete_product(self, name):
            if name in self.inventory:
                del self.inventory(name)
            else:
                print('Товар не найден')
            
    def update_quantity(self, name):
        if name in self.inventory:
            new_quantity = int(input("Введите количество: "))
            self.inventory(name) = new_quantity
        else:
            print('Товар не найден')
    
    def checking_quantity(self, quantity):
        if quantity > 0:
            new_quantity = int(input("Введите количество: "))
            self.inventory(quantity) = new_quantity
        else:
            print('Неверное количество!')