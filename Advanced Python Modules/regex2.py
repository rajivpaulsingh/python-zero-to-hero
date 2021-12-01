"""
PATTERNS

Character	Description	Example Pattern Code	Exammple Match
\d	A digit	file_\d\d	file_25
\w	Alphanumeric	\w-\w\w\w	A-b_1
\s	White space	a\sb\sc	a b c
\D	A non digit	\D\D\D	ABC
\W	Non-alphanumeric	\W\W\W\W\W	*-+=)
\S	Non-whitespace	\S\S\S\S	Yoyo
"""
import re

text = "My telephone number is 809-434-4322"
phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', text)

"""
QUANTIFIERS

Character	Description	Example Pattern Code	Exammple Match
+	Occurs one or more times	Version \w-\w+	Version A-b1_1
{3}	Occurs exactly 3 times	\D{3}	abc
{2,4}	Occurs 2 to 4 times	\d{2,4}	123
{3,}	Occurs 3 or more	\w{3,}	anycharacters
\*	Occurs zero or more times	A\*B\*C*	AAACC
?	Once or none	plurals?	plural
"""
phone_pattern = re.search(r'\d{3}-\d{3}-\d{4}', text)
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern, text)