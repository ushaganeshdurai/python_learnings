class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimenter(self):
        return 2 *(self.width + self.height)
    
    def is_square(self):
        return True if self.height == self.width else False

rect = Rectangle(2,3)
print(rect.area())
print(rect.perimenter())
print(rect.is_square())
