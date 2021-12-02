# Grab all the images in the page

import requests
import bs4

result = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup = bs4.BeautifulSoup(result.text, "lxml")

images = soup.select('.thumbimage') # grab all the elements with that class
print(images[0]['src']) # grabbing the source link of the image

image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Kasparov_Magath_1985_Hamburg-2.png/220px-Kasparov_Magath_1985_Hamburg-2.png')
# image_link.content

# Writing/storing the image in the form of binary content to the local system
f = open('my_computer_image.png', 'wb')
f.write(image_link.content)
f.close()