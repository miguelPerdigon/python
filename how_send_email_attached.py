from os.path import dirname, abspath
from sys import path
from io import BytesIO
from logging import info, error

# to set path of the folder utils
utils_path = '{}/utils'.format(dirname(dirname(abspath('python'))))
path.insert(0, utils_path)

from utils import email_manager

recipients = ['email1@server.com', 'email2@server.com']
cc = ['email3@server.com']
file_buffer = BytesIO()

# is a dict to save several files of different types, key is the name file and the value is the buffer
attached = {
    'book.xlsx': file_buffer,
    'book.csv': file_buffer
}

subject = 'This is a test email'
body = 'If you are not a member for the developer team, please ignore this email.'

sent_email = email_manager.send(recipients, cc, subject, body, attached)

if sent_email:
    info("GREAT!!! We did")
else:
    error("Oops :(")
