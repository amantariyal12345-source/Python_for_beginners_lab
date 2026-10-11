# Q19: Calculate monthly EMI for a loan
principal = float(input("Enter loan amount: "))
annual_rate = float(input("Enter annual interest rate (%): "))
years = int(input("Enter loan period in years: "))

monthly_rate = annual_rate / (12 * 100)
months = years * 12

if monthly_rate == 0:
    emi = principal / months
else:
    emi = principal * monthly_rate * (1 + monthly_rate) ** months / ((1 + monthly_rate) ** months - 1)

print("Monthly EMI =", emi)
