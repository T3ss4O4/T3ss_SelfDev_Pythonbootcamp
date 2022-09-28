# Create a new file Task10c.py which on start awaits for an integer as an input from the user.
# After that, you should get access to your inspirational_quotes.json file and return the quote and author at the index of the user input.
#
# If the user chooses 7, you should return the quote and author of the element #7, not #6.
# After that, the script should end.
#
# Example output:
# >>> User input: 7 | Not all those who wander are lost. - by J. R. R. Tolkien

import json

print("Please enter a Number between 1 and 100 to access your quote of the day!")
number = int(input())
o_file = open("inspirational_quotes.json", "r", encoding="utf-8")

quotes = json.load(o_file)
quote = quotes[number-1]["quote"]
author = quotes[number-1]["author"]

print("Your daily inspiration: " + quote + " - by " + author)
o_file.close()

