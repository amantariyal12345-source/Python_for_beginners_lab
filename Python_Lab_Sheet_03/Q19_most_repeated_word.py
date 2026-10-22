"""Question 19: Find the most repeated word in a string."""

text = input("Enter a sentence: ").lower()
words = text.split()

if not words:
    print("No words were entered.")
else:
    most_common = words[0]
    highest_count = 0

    for word in words:
        count = 0
        for item in words:
            if item == word:
                count += 1
        if count > highest_count:
            highest_count = count
            most_common = word

    print("Most repeated word:", most_common)
    print("Frequency:", highest_count)
