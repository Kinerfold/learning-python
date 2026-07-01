class Inventory:
    
    inventory = {
    "Keyboard": 10,
    "Mouse": 25,
    "Monitor": 5
}
    
    def __init__(self):
        pass
        
    def add_product(self, name, quantity):
        self.inventory[name] = quantity
        
        if "Keyboard" in self.inventory:
            self.inventory[name] = quantity
            print('Товар добавлен!')
                
        if "Mouse" in self.inventory:
            self.inventory[name] = quantity
            print('Товар добавлен!')
            
        if "Monitor" in self.inventory:
            self.inventory[name] = quantity
            print('Товар добавлен!')
        else:
            return 'Товара не существует!'
        
    def show_products(self):
        for key, value in self.inventory.items():
            print(f"{key}: {value}")
        
    def find_product(self, name): 
        if name in self.inventory: 
            print(f"Найден товар: {name}") 
        else: 
            print('Товар не найден')
        
    def delete_product(self):
            if "Monitor" in self.inventory:
                del self.inventory["Monitor"]
             
            if "Mouse" in self.inventory:
                del self.inventory["Mouse"]
             
            if "Keyboard" in self.inventory:
                del self.inventory["Keyboard"]
            else:
                return 'Товара нет!'
            
    def update_quantity(self):
        if "Mouse" in self.inventory:
            new_quantity = int(input("Введите количество: "))
            self.inventory["Mouse"] = new_quantity
            
        if "Keyboard" in self.inventory:
            new_quantity = int(input("Введите количество: "))
            self.inventory["Keyboard"] = new_quantity
            
        if "Monitor" in self.inventory:
            new_quantity = int(input("Введите количество: "))
            self.inventory["Monitor"] = new_quantity
