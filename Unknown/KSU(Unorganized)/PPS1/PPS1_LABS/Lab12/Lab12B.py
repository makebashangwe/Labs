class Dog():
    def __init__(self, age = 0, weight = 0.0, name = '', breed = '', furColor = ''):
        pass

    def bark(self):
        print("Woof! Woof!")

    def rename(self):
        self.name = input(f"{self.name.capitalize()} isn't a very good name. What should they be renamed: ")

    def eat(self):
        while True:
            try:
                food = float(input(f"{self.name.capitalize()} is hungry, how much should he eat: "))
                self.weight += food
                break
            except ValueError:
                print("Please enter an amount in ibs.")

dog = Dog()

print("You are about to create a dog.")

while True:
    try: 
        dog.age = int(input("How old is the dog: "))
        break
    except ValueError:
        print("Please enter a number.")

while True:
    try: 
        dog.weight = float(input("How much does the dog weigh: "))
        break
    except ValueError:
        print("Please enter a number.")

dog.name = input("What is the dog's name: ")
dog.furColor = input("What color is the dog: ")
dog.breed = input("What breed is the dog: ")

print(f"{dog.name.capitalize()} is a {dog.age} year old {dog.furColor} {dog.breed} that weighs {dog.weight} ibs.")
dog.bark()
dog.eat()
dog.rename()
print(f"{dog.name.capitalize()} is a {dog.age} year old {dog.furColor} {dog.breed} that weighs {dog.weight} ibs.")



