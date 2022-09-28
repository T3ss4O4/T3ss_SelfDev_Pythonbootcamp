# In my previous video we started talking about the requests module.
# Create a new file and get familiar working with that module by requesting a page of your choice
# and printing the whole HTML code of it.
# Your code shouldn't be longer than 10 lines.

import requests

content = requests.get('https://theselfdev.com/')

print(content.text)
