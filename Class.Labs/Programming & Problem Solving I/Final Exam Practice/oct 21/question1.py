'''
Question 1: Write a Python program that takes an integer input from the user 
and checks whether the number is positive, negative, or zero using if-else statements. 
Print an appropriate message for each case.
'''

n = input("Please enter a number: ")

if not n.isalpha():
    if int(n) < 0:
        print("Number is negative")
    elif int(n) == 0:
        print("Number is zero")
    elif int(n)>0:
        print("Number is positive.")
else:
    print("Incorrect Format.")


#Suggestions: try/catch

'''
n = input("Please enter a number: ")

try:
    num = int(n)
    if num < 0:
        print("Number is negative")
    elif num == 0:
        print("Number is zero")
    else:
        print("Number is positive.")
except ValueError:
    print("Incorrect format. Please enter a valid integer.")
    '''