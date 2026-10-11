# Q28: Check whether a character is uppercase, lowercase, or a digit
character = input("Enter a character: ")

if len(character) != 1:
    print("Please enter exactly one character.")
elif character.isdigit():
    print("Digit")
elif character.isupper():
    print("Uppercase letter")
elif character.islower():
    print("Lowercase letter")
else:
    print("Special character")
