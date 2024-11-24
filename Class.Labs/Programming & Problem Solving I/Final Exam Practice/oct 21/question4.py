'''
Question 1: Write a Python program that prints the numbers from 1 to 50 
using a for loop. However, for multiples of 3, print "Fizz" instead of the 
number, and for multiples of 5, print "Buzz." For numbers that are multiples 
of both 3 and 5, print "FizzBuzz."
'''

def fizzbuzz():
    for i in range(1,51):
        if i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz()