# Install pillow (Python Image Library) to work with images
# pip install pillow

from PIL import Image

# Opening images
mac = Image.open('example.jpg')
print(type(mac))

mac.show()
print(mac.size)
print(mac.format)
print(mac.format_description)


# Cropping Images
pencils = Image.open('pencils.jpg')
print(pencils.size)

x = 0
y = 0
w  = 1950 / 3
h = 1300 / 10

cropped_pencils = pencils.crop((x,y,w,h))
cropped_pencils.show()


# Grab mac photo
halfway = 1993/2
x = halfway - 200
w = halfway + 200

y = 800
h = 1257

cropped_mac = mac.crop((x,y,w,h))
cropped_mac.show()


# Copying and Pasting Images
computer = mac.crop((x,y,w,h))
copied_mac = mac.paste(im=computer, box=(0,0))
mac.show()

copied_mac = mac.paste(im=computer, box=(796,0))
mac.show()


# Resizing Images
resized_mac = mac.resize((2000,500))
resized_mac.show()


# Rotate Images
rotated_mac = mac.rotate(120)
rotated_mac.show()


# Transparency
red = Image.open('red_color.jpg')
red.show()

faded_red = red.putalpha(128)
red.show()


# Saving Images
red.save('purple.png')