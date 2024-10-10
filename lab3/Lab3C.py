small = int(input("Enter the number of small sandwiches: "))
medium = int(input("Enter the number of medium sandwiches: "))
large = int(input("Enter the number of large sandwiches: "))
xLarge = int(input("Enter the number of extra-large sandwiches: "))

print(f"\nYou've entered {small} small sandwiches.")
print(f"You've entered {medium} medium sandwiches.")
print(f"You've entered {large} large sandwiches.")
print(f"You've entered {xLarge} extra-large sandwiches.")

small = small * 30
medium = medium * 60
large = large * 75
xLarge = xLarge * 135
total_seconds = small + medium + large + xLarge
minutes = total_seconds // 60
seconds = total_seconds % 60

print(f"\nTotal cooking time is {minutes} minutes and {seconds} seconds.")

