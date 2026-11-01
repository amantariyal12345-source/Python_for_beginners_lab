# Question 13: Write a program to read numbers from a file and display their sum and average.
# Create numbers.txt with one number per line, for example: 10, 20, 30.
try:
    with open("numbers.txt", "r", encoding="utf-8") as file:
        numbers = [float(line.strip()) for line in file if line.strip()]
    if numbers:
        print("Sum:", sum(numbers))
        print("Average:", sum(numbers) / len(numbers))
    else:
        print("numbers.txt contains no numbers.")
except FileNotFoundError:
    print("numbers.txt was not found. Create it with one number per line.")
except ValueError:
    print("Please ensure numbers.txt contains only valid numbers, one per line.")
except OSError as error:
    print(f"File error: {error}")
