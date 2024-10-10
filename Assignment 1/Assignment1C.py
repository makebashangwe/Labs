''' Class: CSE 1321L
Section: J51
Term: FALL 2024
Name: Makeba Waddy
ASSIGNMENT 1'''

weight = float(input("What is your weight in KG: "))
height = float(input("What is your height in m: "))
height = (height/100)
height = (height ** 2)

BMI = round(weight / height, 1)

match (BMI):
    case BMI if BMI <= 18.5:
        print(f"""Your BMI is {BMI}.
You are classified as: 1 weight""")
    case BMI if BMI >= 18.5 or BMI <= 24.9:
        print(f"""Your BMI is {BMI}.
You are classified as: 2 weight""")
    case BMI if BMI >= 25 or BMI <= 29.9:
        print(f"""Your BMI is {BMI}.
You are classified as: 3 weight """)
    case BMI if BMI >= 29.9:
        print(f"""Your BMI is {BMI}. 
You are classified as: 4 weight""")