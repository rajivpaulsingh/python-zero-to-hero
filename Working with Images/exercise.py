# Reveal the secret message using the two images (word_matrix and mask)

from PIL import Image

words = Image.open('word_matrix.png')
words.show()

mask = Image.open('mask.png')
mask.show()

# Resize the images to match
mask.size
words.size

mask = mask.resize((1015,559))

# Add in alpha parameter
new_mask = mask.putalpha(200)
mask.show()

pasted_words = words.paste(mask, (0,0), mask)
words.show()