# Grab all the links in the table of content

import requests
import bs4

result = requests.get("https://en.wikipedia.org/wiki/Grace_Hopper")
soup = bs4.BeautifulSoup(result.text, "lxml")

soup.select('.toctext') # grab all the elements with that class .toctext

first_item = soup.select('.toctext')[0]
print(first_item.getText()) # first item

# print all the items
for items in soup.select('.toctext'):
    print(items.getText())