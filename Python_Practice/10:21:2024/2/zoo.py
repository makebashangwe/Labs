class Animal:
    def __init__(self):
        pass
    def speak(self):
        return "*Generic Sound*"
    def move(self):
        return "*walks*"

class Dog(Animal):
    def speak(self):
        return "Woof!"
    def move(self):
        return "*runs*"
    
class Cat(Animal):
    def speak(self):
        return "Meow!"
    def move(self):
        return "*sneaks*"
