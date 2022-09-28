# Create a new file Task10a.py and scrape all members of the page https://theselfdev.com/community.
# Your goal is to get all possible data which is visible on the webpage about one single member.
#
# Those include:
# - Name
# - Category
# - One-line Pitch
# - Image URL
#
# Find a way by using the packages requests and beautifulsoup to scrape all the members and save them all in a data type which fits your needs.
# Remember what data types we discussed before and be reasonable why you decided to use that specific data type.
# After that, save the data you scraped in a new file called community_members.json.

import requests
import json
from bs4 import BeautifulSoup

members = []
content = requests.get('https://theselfdev.com/community')
soup = BeautifulSoup(content.text, "html.parser")

for entry in soup.select(".creator-card-wrapper"):
    member = {}

    entry_name = entry.select_one(".name").text.strip()
    member["name"] = entry_name

    entry_category = entry.select_one(".category").text.strip()
    member["category"] = entry_category

    entry_summary = entry.select_one(".summary").text.strip()
    member["pitch"] = entry_summary

    # having problems with scraping the image url

    members.append(member)


o_file = open("community_members.json", "w", encoding="utf-8")

o_file.write(json.dumps(members, indent=4))

o_file.close()

