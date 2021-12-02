"""
GOAL: Get the title of every book which has 2 star ratings
"""

import requests
import bs4

base_url = 'https://books.toscrape.com/catalogue/page-{}.html'

# Rough work
page_number = 12
print(base_url.format(page_number)) # example of page number 12

res = requests.get(base_url.format(1))
soup = bs4.BeautifulSoup(res.text, 'lxml')
products = soup.select('.product_pod')
example = products[0]
print(example.select('.star-rating.Three'))

"""
- We can check if something is 2 stars (string call in or example.select(rating))
- example.select('a')[1]['title'] to grab the book title
"""
# Real solution
two_stars_titles = [] # empty list to begin with

for n in range(1, 51):

    srcape_url = base_url.format(n)
    res = requests.get((srcape_url))

    soup = bs4.BeautifulSoup(res.text, 'lxml')
    books = soup.select(".product_pod")

    for book in books:
        if len(book.select('.star-rating.Two')) != 0:
            book_title = book.select('a')[1]['title']
            two_stars_titles.append(book_title)

print(two_stars_titles)