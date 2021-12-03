"""
TASK 1
"""

import csv
from os import link

data = open('Exercise_Files/find_the_link.csv', encoding='utf-8')
csv_data = csv.reader(data)
data_lines = list(csv_data)

#print(data_lines)

# Create the google drive link
# Method 1
link_list = []

for row_num, data in enumerate(data_lines):
    link_list.append(data[row_num])
''.join(link_list)

print(link_list)


# Method 2
link_str = ''
for row_num, data in enumerate(data_lines):
    link_str += data[row_num]

print(link_str)



"""
TASK 2
"""
import PyPDF2

f = open('Exercise_Files/Find_the_Phone_Number.pdf', 'rb')
pdf = PyPDF2.PdfFileReader(f)
print(pdf.numPages)

# Phone number matching - start with 3 digits in a row
import re
pattern = r'\d{3}'

all_text = ''

for n in range(pdf.numPages):
    page = pdf.getPage(n)
    page_text = page.extractText()

    all_text = all_text + ' ' + page_text

# Get all the matches to get the correct pattern
for match in re.finditer(pattern, all_text):
    print(match)

print(all_text[41790:41808+20])

# Now we get to the solution
import re

pattern = r'\d{3}.\d{3}.\d{4}'

for n in range(pdf.numPages):
    page = pdf.getPage(n)
    page_text = page.extractText()
    match = re.search(pattern, page_text)

    if match:
        print('The phone number is: {}'.format(match.group()))
