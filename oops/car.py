class Dog:
    def __init__(self,color,breed):
        self.color = color
        self.breed = breed


    def introduce(self):
        print(f"Color: {self.color}, Breed: {self.breed}")

buddy = Dog("Brown","Daschund")
buddy.introduce()


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print(f"Hello, my name is {self.name}")
    def have_birthday(self):
        self.age+=1
        return self.age
p1 = Person("Richard",20)
p1.greet()
returned_age = p1.have_birthday()
print(returned_age)
