# Question 7: Write a program to write multiple lines of input from the user into a file.
# Enter a blank line when you have finished entering text.
try:
    print("Enter text lines. Press Enter on an empty line to finish:")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    with open("user_input.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(lines))
        if lines:
            file.write("\n")
    print("Input saved to user_input.txt.")
except OSError as error:
    print(f"File error: {error}")
