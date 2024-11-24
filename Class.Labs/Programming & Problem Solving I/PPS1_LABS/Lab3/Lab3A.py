principal = float(input("Amount Owed: $"))
APR = float(input("APR: "))

monthly_percentage = APR / 12

monthly_percentage = round(monthly_percentage, 3)
print(f"Monthly percentage rate: {monthly_percentage}")

APR = APR/100
minimum_payment = principal * APR / 12
minimum_payment = round(minimum_payment, 2)

print(f"Minimum payment: ${minimum_payment}")
