"""Question 26: Check if two dictionaries are equal."""

def read_dictionary(label):
    data = {}
    count = int(input("How many entries in " + label + "? "))
    for index in range(count):
        key = input("Enter key: ")
        value = input("Enter value: ")
        data[key] = value
    return data

first = read_dictionary("the first dictionary")
second = read_dictionary("the second dictionary")

if first == second:
    print("The dictionaries are equal.")
else:
    print("The dictionaries are not equal.")
