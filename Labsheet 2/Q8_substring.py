# Q8: Check if a string contains a particular substring
text = input("Enter the main string: ")
substring = input("Enter the substring: ")

if substring in text:
    print("Substring found.")
else:
    print("Substring not found.")
