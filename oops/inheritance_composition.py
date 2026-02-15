class Address:

    def __init__(self,street,city,zipcode):
        self.street = street
        self.city = city
        self.zipcode=zipcode

    def display(self):
        return f"{self.street}, {self.city}, {self.zipcode}"


class Person:
    def __init__(self,name,street,city,zipcode):
        self.name=name
        #composition - created address object inside person class but it should be done within __init__ method only!!!
        self.address = Address(street,city,zipcode)

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"{self.address.display()}")

person = Person("Alice","123 st","Chennai",600033)

            
class CPU:

    def __init__(self,brand,cores):
        self.brand = brand
        self.cores = cores

    def info(self):
        return f"{self.brand} {self.cores}"


class RAM:
    def __init__(self,size):
        self.size = size

    def info(self):
        return f"{self.size}"

class SSD:
    def __init__(self,capacity):
        self.capacity=capacity

    def info(self):
        return f"{self.capacity}"

class Computer:
    def __init__(self,model,size,capacity,brand,cores):
        #using CPU
        self.cpu=CPU(brand,cores)
        #using RAM
        self.ram = RAM(size)
        #using SSD
        self.ssd = SSD(capacity)
        #own attribute
        self.model=model
    
    def display_comp_info(self):
        print(f"{self.model}")
        print(f"{self.cpu.info()}")
        print(f"{self.ram.info()}")
        print(f"{self.ssd.info()}")


comp = Computer("Asus","8GB",512,"AMD",12)
comp.display_comp_info()





    




