while True:
    try: 
        age = int(input("Enter your age:  "))
        break
    except ValueError:
        print("Please enter a number.")
if age < 13:
    print("Child")
elif 13 <= age < 19:
    if age ==  16:
       print("Sweet Sixteen!")
    elif age ==18:
        print("You're an adult now!")
    print("Teen.")
else:
    print("Adult.")