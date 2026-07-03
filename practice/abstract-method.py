from abc import ABC, abstractmethod
import math

# ---------------------------------------------------------------------------------------

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius=0):
        self.radius = radius
    
    def area(self):
        return self.radius * self.radius * math.pi
    
    def perimeter(self):
        return 2 * self.radius * math.pi
            
class Triangle(Shape):
    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c
    
    def perimeter(self):
        return self.a + self.b + self.c
    
    def area(self):
        pass

# ---------------------------------------------------------------------------------------

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return 'ГАВ!'

class Cat(Animal):
    def make_sound(self):
        return 'МЯУ!'

class Bird(Animal):
    def make_sound(self):
        return 'КАР!'

dog = Dog()
cat = Cat()
bird = Bird()

rec = Rectangle(30, 50)
circ = Circle(30)
trian = Triangle(10, 10, 10)

print(dog.make_sound())
print(cat.make_sound())
print(bird.make_sound())

print(rec.area())
print(circ.area())
print(trian.perimeter())