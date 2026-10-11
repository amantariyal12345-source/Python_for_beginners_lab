# Q13: Calculate compound interest
principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual rate (%): "))
time = float(input("Enter time in years: "))

amount = principal * (1 + rate / 100) ** time
compound_interest = amount - principal

print("Compound Interest =", compound_interest)
print("Amount =", amount)
