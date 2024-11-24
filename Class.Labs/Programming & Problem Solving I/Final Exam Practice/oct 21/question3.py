'''
Question 3: Write a Python program to determine if a given year is a leap year. 
A year is a leap year if it is divisible by 4 but not divisible by 100, or it is 
divisible by 400.

'''

year = input("Please enter the year.")
leapyear = False

if not year.isalpha():
    year = int(year)
    if year % 4 == 0 or (year % 400 == 0 and not year % 100 == 0):
        leapyear = True
    else:
        leapyear = False
else:
    print("Invalid Format")

print(leapyear)