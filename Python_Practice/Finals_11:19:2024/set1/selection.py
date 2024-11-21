n = int(input("Enter a number: "))
if n > 10 and n % 2 == 0:
    print("This number is even and greater than 10.")
elif n <= 10 and n % 2 != 0:
    print("This number is odd and less than or equal to 10.")
else:
    print("None of the above.")