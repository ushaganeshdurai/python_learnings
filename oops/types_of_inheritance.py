#single inheritance:

class Animal:

    def __init__(self,name):
        self.name=name

    def sound(self):
        return "Makes sound"


class Dog(Animal):

    def bark(self):
        return f"{self.name} barks!"

dog = Dog("Buddy")
print(dog.bark())


#multiple inheritance

class Dollar:
    def value(self):
        return "90rs"

class INR:
    def value(self):
        return "1dollar"

class Currency(Dollar,INR):
    def calc(self):
        return "Nothing"

curr = Currency()
#MRO -- since I called Dollar first 90rs prints
print(curr.value())
print(curr.calc())

#multilevel inheritance 
class Grandparent:
    def family_name(self):
        return "Smith"

class Parent(Grandparent):
    def profession(self):
        return "Engineer"

class Child(Parent):
    def age(self):
        return 10

child = Child()
print(child.family_name())  
print(child.profession())   
print(child.age())

#Hierarchicla inheritance

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def type(self):
        return "Car"

class Bike(Vehicle):
    def type(self):
        return "Bike"

car = Car("Toyota")
bike = Bike("Honda")
print(f"{car.brand} - {car.type()}")  
print(f"{bike.brand} - {bike.type()}")


