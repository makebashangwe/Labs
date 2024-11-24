class Car:
    def __init__(self,make,model,licensePlate):
        self.make = make
        self.model = model
        self.licensePlate = licensePlate
        self.isRented = False


class CarRental:
    def __init__(self):
        self.cars = [] #list of cars
    
    def list_cars (self): 
        if not self.cars:
            print("No cars available in the rental service.")
        else:
            for car in self.cars:
                print()
                status = "Rented" if car.isRented else "Available"
                print(f"{car.make.capitalize()} {car.model.capitalize()} ({car.licensePlate}): {status}")
                print()

    def add_car(self, car):
        self.cars.append(car)
        print(f"'{car.model.capitalize()} {car.make.capitalize()}' has been added.")

    def remove_car(self,car):
        self.cars.remove(car)
        print(f"'{car.model.capitalize()} {car.make.capitalize()}'has been removed")

    def rent_car(self,car):
        if car.isRented == False and car in self.cars:
            car.isRented = True
        elif car.isRented == True:
            print(f"'{car.model.capitalize()} {car.make.capitalize()}' is already rented." )
        else:
            print(f"'{car.model.capitalize()} {car.make.capitalize()}' does not exist.")

    def return_car(self,car):
        if car.isRented != False and car in self.cars:
            car.isRented = False
            print(f"'{car.model.capitalize()} {car.make.capitalize()}' has been returned.")
        elif car.isRented == False:
            print("Car is already returned.")
    

#test objects:
# Creating the CarRental instance

rental_service = CarRental()

# Creating Car objects
car1 = Car("Toyota", "Corolla", "ABC-123")
car2 = Car("Honda", "Civic", "XYZ-789")
car3 = Car("Ford", "Focus", "LMN-456")

# Testing the methods
rental_service.add_car(car1)
rental_service.add_car(car2)
rental_service.add_car(car3)

# Rent out some cars
rental_service.rent_car(car1)
rental_service.rent_car(car2)

# List current status of cars
rental_service.list_cars()

# Return a car
rental_service.return_car(car1)

# List cars again after returning one
rental_service.list_cars()

# Attempt to remove a car that is still rented
rental_service.remove_car(car2)

# Remove a car that has been returned
rental_service.remove_car(car1)

# Final list to verify state
rental_service.list_cars()
