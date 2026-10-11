# Q29: Check if a number is in a given range
number = float(input("Enter a number: "))
lower = float(input("Enter lower limit: "))
upper = float(input("Enter upper limit: "))

if lower <= number <= upper:
    print("Number is within the range.")
else:
    print("Number is outside the range.")
