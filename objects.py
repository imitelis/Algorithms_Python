# Initializing a Class:
class MyClass:
    # Class constructor (initialization method)
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2
    
    # Class method
    def my_method(self):
        return "This is a method inside MyClass"

# Creating objects of MyClass
obj1 = MyClass("value1", "value2")
obj2 = MyClass("another value", "yet another value")

# Accessing object attributes and methods
print(obj1.attribute1)  # Output: "value1"
print(obj2.attribute2)  # Output: "yet another value"
print(obj1.my_method())  # Output: "This is a method inside MyClass"


# Inheritances:
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass  # Abstract method, to be overridden by subclasses

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog("Buddy")
print(dog.speak())  # Output: "Woof!"

cat = Cat("Whiskers")
print(cat.speak())  # Output: "Meow!"


# Polymorphisms:
class Shape:
    def area(self):
        pass  # Abstract method, to be overridden by subclasses

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

shapes = [Square(4), Circle(3)]
for shape in shapes:
    print("Area:", shape.area())