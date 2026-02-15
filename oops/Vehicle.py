class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")


class Car(Vehicle):
    def __init__(self, brand, model, year, no_of_doors):
        # First, initialize the parent class
        super().__init__(brand, model, year)
        # Then, add the child-specific attribute
        self.no_of_doors = no_of_doors
    
    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Doors: {self.no_of_doors}")


class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, has_sidecar):
        # Initialize parent class
        super().__init__(brand, model, year)
        # Add child-specific attribute
        self.has_sidecar = has_sidecar
    
    def display_info(self):
        sidecar_status = "Yes" if self.has_sidecar else "No"
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Sidecar: {sidecar_status}")

class Truck(Vehicle):
    def __init__(self,brand,model,year,cargo_capacity,is_commercial):
        super().__init__(brand,model,year)
        self.cargo_capacity=cargo_capacity
        self.is_commercial=is_commercial

    def display_info(self):
        print(f"{self.brand} {self.model} {self.year} {self.cargo_capacity} {self.is_commercial}")


# Test the classes
car1 = Car("Toyota", "Camry", 2023, 4)
car1.display_info()

motorcycle1 = Motorcycle("Harley-Davidson", "Street 750", 2022, False)
motorcycle1.display_info()

truck1 = Truck("mahindra","heavyduty",2020,600,True)
truck1.display_info()
