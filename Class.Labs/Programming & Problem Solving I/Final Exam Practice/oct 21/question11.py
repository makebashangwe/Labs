'''
Question 4: Write a Python program that defines a method called greet_user 
which takes a string parameter (the user's name) and prints a greeting message. 
Call the function with the inputted name.
'''
def greet_user (name):
    return print(f"Hello, {name}!")

name = input("What's your name?: ").capitalize()
greet_user(name)