"""
OR operator |
"""
import re

re.search(r"cat | dog", "The dog is here")

"""
Wildcard operator
"""
re.findall(r".at","The cat in the hat sat here.")
re.findall(r".at","The bat went splat")
re.findall(r"...at","The bat went splat")
re.findall(r'\S+at',"The bat went splat")

"""
Starts with and Ends with
"""
re.findall(r'^\d','1 is the loneliest number.') # starts with
re.findall(r'\d$','This ends with a number 2') # ends with

"""
Exclusion
"""
phrase = "there are 3 numbers 34 inside 5 this sentence."
re.findall(r'[^\d]',phrase)

# Best way to get rid of punctuations
test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
re.findall('[^!.? ]+',test_phrase)

"""
Brackets for grouping
"""
text = 'Only find the hypen-words in this sentence. But you do not know how long-ish they are'
re.findall(r'[\w]+-[\w]+',text)

"""
Parenthesis for Multiple Options
"""
# Find words that start with cat and end with one of these options: 'fish','nap', or 'claw'
text = 'Hello, would you like some catfish?'
texttwo = "Hello, would you like to take a catnap?"
textthree = "Hello, have you seen this caterpillar?"

re.search(r'cat(fish|nap|claw)',text)
re.search(r'cat(fish|nap|claw)',texttwo)
re.search(r'cat(fish|nap|claw)',textthree)