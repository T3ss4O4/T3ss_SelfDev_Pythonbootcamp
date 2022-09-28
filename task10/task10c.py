# This task assumes you already know what an API is but haven’t worked with one yet.
#
# To do that, I dived into the list of public APIs from GitHub and chose one which contains many inspirational quotes.
#
# Your goal is to build a script which requests the API through this link: https://api.goprogram.ai/inspiration
#
# How do you start?
# First, you need to request the API with the request package (surprise, surprise) like you have learned before. After that you have to replace the URL with that mentioned link above, which we now refer to as an endpoint from now on.
#
# If you do that correctly, you should get the following string as a return:
# '{"quote": "Not all those who wander are lost.", "author": "J. R. R. Tolkien”}'
#
# Your task now is to build a script which requests the API every 5 seconds and saves the quote and author of the returned string into a list of dictionaries. If the list reached 100 entries, you shall stop the loop and save the whole list of dictionaries into a file called inspirational_quotes.json.
#
# In the end you should have a new file which contains 100 inspirational quotes as a dictionary (json format).

import requests
import time
import json

inspiration = requests.get("https://api.goprogram.ai/inspiration").json()
quotes = []
i = 0

while i < 100:
    quotes.append(inspiration)
    i += 1
    time.sleep(5)

o_file = open("inspirational_quotes.json", "w", encoding="utf-8")

o_file.write(json.dumps(quotes, indent=4))

o_file.close()
