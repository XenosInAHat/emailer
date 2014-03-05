emailer
=======

A quick and dirty email sending script to send email out to a list of 
individuals.

Execution Notes:

Currently, this code works for Python 2.7.5 on OS X 10.9.2. Due to
the differences between Python2 and Python3, this code will NOT
work for Python3. (It's possible that the only necessary changes would
be adding parentheses to the print statements, as well as altering the
importing of the Tkinter module.)

Additionally, this code currently utilizes Gmail's SMTP servers to send
emails. This also requires that you have a Gmail account to use this
'as is.' You should be able to change this pretty easily by changing the
server information to 'localhost' or any other SMTP server.

To run the code correctly, you will need a file full of comma-separated
names and email addresses. I used a '.txt' file, but a '.csv' should
work.

You will also need a file which includes the body of the email you will
be sending. I used a quick and dirty '.txt' file with HTML tags (I have
no idea what I'm doing) to create this, but a standard HTML file would
probably work.

The program usage information is output upon execution, but I'll also
post it here:

    python emailer.py <name_file> <username> <password> <message_file>
