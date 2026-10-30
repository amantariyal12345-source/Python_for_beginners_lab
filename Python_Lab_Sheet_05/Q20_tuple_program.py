"""
Question 20: Find the length of the longest word in a tuple.
Python Programming Lab Sheet 05 - Tuples Operations
"""

# Find the length of the longest word
words = ("apple", "watermelon", "banana", "strawberry")
longest_length = max(len(word) for word in words)
print("Words:", words)
print("Length of longest word:", longest_length)
