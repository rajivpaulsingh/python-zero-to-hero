
import csv

"""
Common error that happens a lot
"""
# Open the file
data = open('example.csv')

# csv.reader
csv_data = csv.reader(data)

# reformat it into a pythong object list of lists
data_lines = list(csv_data)

# The above results in the UnicodeDecodeError: 'charmap codec can't decode.... (usally due to @ character)
# fix it by adding the below parameter

"""
Reading CSF files
"""
data = open('example.csv', encoding='utf-8')
csv_data = csv.reader(data)
data_lines = list(csv_data)
print(data_lines[:3])

for line in data_lines[:5]:
    print(line)

print(data_lines[10]) # for 10th data point/row
print(data_lines[10][3]) # for 4rth field of 10th row

# To get a single column (emails)
all_emails = []

for line in data_lines[1:15]:
    all_emails.append(line[3])

print(all_emails)

# To get the list of full names (first + last)
full_names = []

for line in data_lines[1:10]:
    full_names.append(line[1] + ' ' + line[2])

print(full_names)


"""
Writing to CSV files
"""
# New file
file_to_output = open('to_save_file.csv', mode='w', newline='')
csv_writer = csv.writer(file_to_output, delimiter=',')

csv_writer.writerow(['a','b','c']) # single row
csv_writer.writerows([['1','2','3'],['4','5','6']]) # multiple rows
file_to_output.close()

# Existing file
f = open('to_save_file.csv', 'a', newline='')
csv_writer = csv.writer(f)

csv_writer.writerow(['new','new,','new'])
f.close()