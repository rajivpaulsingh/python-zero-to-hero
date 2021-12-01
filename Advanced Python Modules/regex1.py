text = "The agent's phone number is 478-485-3453. Call soon!"

print('phone' in text) # Simple way

# Using regex
import re

pattern1 = 'phone'
pattern2 = 'NOT IN TEXT'
print(re.search(pattern1, text))
print(re.search(pattern2, text))

match = re.search(pattern1, text)
print(match.start())
print(match.end())


text2 = "my phone once, my phone twice"
matches = re.findall('phone', text2)
print(matches)
print(len(matches))