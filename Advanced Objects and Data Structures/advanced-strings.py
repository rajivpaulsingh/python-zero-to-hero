s = 'hello world'

# Changing case
print(s.capitalize())
print(s.upper())
print(s.lower())


# Location and Counting
print(s.count('o'))
print(s.find('o'))


# Formatting
print(s.center(20, 'z'))
print('hello\thi'.expandtabs())


# is check methods
s = 'hello'
print(s.isalnum())
print(s.isalpha())
print(s.islower())
print(s.isspace())
print(s.istitle())
print(s.isupper())
print(s.endswith('o'))
print(s[-1] == 'o')


# Built-in Regex
print(s.split('e'))
print(s.partition('l'))