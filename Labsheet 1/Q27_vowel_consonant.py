# Q27: Check whether a character is a vowel or consonant
character = input("Enter a character: ")

if len(character) == 1 and character.isalpha():
    if character.lower() in "aeiou":
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Please enter a single alphabetic character.")
