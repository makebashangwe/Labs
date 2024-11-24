''' Class: CSE 1321L
Section: J51
Term: FALL 2024
Name: Makeba Waddy
ASSIGNMENT 1'''

principal = float(input("Enter the loan amount: "))

interest = float(input("Enter the annual interest rate (in %): "))
interest = interest / 100
monthlyInterest = float(interest / 12)

term = int(input("Enter the loan term (in years): "))
numOfpayments = term*12

monthlyPayment = (principal*monthlyInterest)
monthlyPayment2 = monthlyPayment * (1+monthlyInterest)**numOfpayments
monthlyPayment3 = (1+monthlyInterest)**numOfpayments - 1
monthlyPayment4 = monthlyPayment2 / monthlyPayment3
print(round(monthlyPayment4, 2))