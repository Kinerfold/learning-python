import json

class Inventory:

    def __init__(self):
        self.inventory = {
            "Keyboard": 10,
            "Mouse": 25,
            "Monitor": 5
        }
        
    def add_product(self, name, quantity):
        if name not in self.inventory:
            print('Товар не найден!')
        else:
            self.inventory[name] = quantity
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
             print('Товар удалён!')
        else:
            print('Товар не найден!')
            
    def update_quantity(self, name):
        if name not in self.inventory:
            print('Товар не найден!')
        else:
            new_quantity = int(input("Введите количество: "))
            self.inventory[name] = new_quantity
    
    def checking_quantity(self, name):
        new_quantity = int(input("Введите количество: "))
        if new_quantity >= 0:
            self.inventory[name] = new_quantity
            print(f'Количество изменено!')
        else:
            print('Неверное количество!')
    
    def all(self):
        for item in self.inventory:
            print(item)
    
    def clear(self):
        self.inventory.clear()
        print(self.inventory)
    
    def save_data(self):
        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(self.inventory, file)
        
        print('Данные записаны в файл json')
    
    def load_data(self):
        with open('data.json', 'r', encoding='utf-8') as file:
            self.inventory = json.load(file)
        
        print('Данные загружены')