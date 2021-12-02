"""
Complete the tasks below
"""

# Task 1: Import the libraries needed to scrape
import requests
import bs4

# Task 2: Use requests library and BeautifulSoup to connect to http://quotes.toscrape.com/ 
# and get the HMTL text from the homepage.
res = requests.get("http://quotes.toscrape.com/")
soup = bs4.BeautifulSoup(res.text, 'lxml')

# Task 3: Get the names of all the authors on the first page.
authors = set() # using set to avoid duplicates
for name in soup.select('.author'):
    authors.add(name.text)

print(authors)

# Task 5: Create a list of all the quotes on the first page
quotes = []

for quote in soup.select('.text'):
    quotes.append(quote.text)

print(quotes)

# Task 6: Create a list of the top ten tags from the top right of the home page
top_ten = []

for tag in soup.select(".tag-item"):
    top_ten.append(tag.text)

print(top_ten)


# Task 7: All the authors in the website

base_url = "http://quotes.toscrape.com/page/"
authors = set()

for page in range(1, 10):

    page_url = base_url + str(page)
    res = requests.get(page_url)
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    for name in soup.select('.author'):
        authors.add(name.text)

print(authors)
