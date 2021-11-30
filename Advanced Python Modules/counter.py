# Count the number of unique items in the list
# Using counters which is a disctionary subclass (special dictionary)
from collections import Counter

mylist = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 'a', 'a', 'a']
sentence = "How many times each word show up in this sentence"

# Run
print(Counter(mylist))

print(Counter('aaaabbbkkkkkssss'))

print(Counter(sentence.split()))

# Most common
c = Counter(sentence)
print(c.most_common(3))