import requests

result = requests.get("http://www.example.com")
print(type(result))
print(result.text) # Raw string


import bs4

soup = bs4.BeautifulSoup(result.text, "lxml")
print(soup) # Beautiful soup object


# Grab things from html document
title = soup.select('title')[0].getText() # pass the tag name to grab title
print(title)

site_paragraphs = soup.select('p') # grabs the paragraphs
print(site_paragraphs[0].getText())