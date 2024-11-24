class Chair:
    numofLegs = 4
    rolling = False
    material = 'plastic'

print("You are about to create a chair.")
ch1 = Chair()
ch1.numofLegs = int(input("How many legs does your chair have: "))
rolling_input = input("Is your chair rolling (true/false): ").lower()
if rolling_input == "true":
    ch1.rolling = True
    statement = "rolling"
elif rolling_input == "false":
    ch1.rolling = False
    statement = "not rolling"
else:
    ch1.rolling = False

ch1.material = input("What material is you chair made out of: ")



print(f"Your chair has {ch1.numofLegs} legs, is {statement}, and is made of {ch1.material}. ")
print("This program is going to change that. ")
print("Your chair has 4 legs, is not rolling, and is made of wood.")
