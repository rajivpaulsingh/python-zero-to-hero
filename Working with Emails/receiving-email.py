"""
To do we will use the built-in imaplib library. 
We will also use the built in email library for parsing through the recieved emails.
"""

import imaplib

M = imaplib.IMAP4_SSL('imap.gmail.com')

import getpass

email = input("Enter your email: ")
# Remember you need an ap password if you are a gmail user
password = getpass.getpass("Enter your password: ")

M.login(email, password)
M.list() # To see all the things that can be checked in gmail

# Connect to your inbox
M.select("inbox")

# Searching the inbox
typ, data = M.search(None, 'BEFORE 01-Nov-2021')
# typ, data = M.search(None, 'FROM user@test.com')
print(typ)
print(data)

# typ, data = M.fetch(data[0],"(RFC822)")
result, email_data = M.fetch(data[0], "(RFC822)")
raw_email = email_data[0][1]
raw_email_string = raw_email.decode('utf-8')

# Use the built in email library to help parse this raw string
import email
email_message = email.message_from_string(raw_email_string)

for part in email_message.walk():
    if part.get_content_type() == "text/plain":
        body = part.get_payload(decode=True)
        print(body)