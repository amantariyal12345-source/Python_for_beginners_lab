"""Write a program to find unique words in a sentence using a set."""

# Q26. Find unique words in a sentence using a set
# Words are converted to lowercase so that Python and python count as one word.

sentence = input("Enter a sentence: ")
words = sentence.lower().split()
unique_words = set(words)

print("Unique words:", unique_words)
print("Number of unique words:", len(unique_words))
