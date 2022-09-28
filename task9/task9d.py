# Now that you have the HTML code of your whole webpage,
# find a way to count all "e"s in that whole HTML code and print the number of counts.
# Do the same for the word "<p>" and print the number of counts as well.
import requests
from bs4 import BeautifulSoup

content = requests.get('https://theselfdev.com/')

letter_e = 0
for character in content.text:
    if character == 'e':
        letter_e += 1

print('Number of e in html-text of selfdev website:', letter_e)

soup = BeautifulSoup(content.text)
print('Number of p-tags in html-text of selfdev website:', len(soup.findAll('p')))


