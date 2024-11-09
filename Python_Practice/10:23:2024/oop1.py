class Car:
    def __init__(self, make, model, year, mileage = 0, fuel_level = 50):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.fuel_level = fuel_level
    def drive(self,distance):
        if self.fuel_level > 0 and distance/10 - self.fuel_level > 0:
            self.fuel_level = distance/10 - self.fuel_level 
        else:
            print("Your tank is empty!")
    def refuel(self,amount):
        if amount + self.fuel_level < 50:
            self.fuel_level = amount + self.fuel_level
        else:
            print("The tank is full.")
    def describe_car(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Mileage: {self.mileage}, Fuel Level: {self.fuel_level}")



car = Car() 
car.make = input("What is the make: ")
car.model = input("What is the model: ")
car.year = input("What is the year: ")
while True:
    try:
        car.mileage = float(input("What is the mileage: "))
        break
    except ValueError:
        print("Enter a number.")
while True:
    try:
        car.fuel_level = float(input("What is the fuel level (default: 50): "))
        break
    except ValueError:
        print("Enter a number.")


car.drive()
car.refuel()
car.describe_car()


