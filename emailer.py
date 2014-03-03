"""
Written by: Kirk Smith

Code segments and examples found and used from:
    tutorialspoint: tutorialspoint.com
    Justin Duke: jmduke.com

This is free and unencumbered software released into the public domain.
"""

# Modules used to create the GUI
from Tkinter import *
import tkMessageBox
import Tkinter

# Module to login to Gmail's SMTP server and create and send emails.
import smtplib

# Module to allow access to command line arguments.
import sys

# List of names of individuals to send emails
names = []
# List of email addresses to be used as recipients
email_addresses = []
# List of items (as ints) chosen from the listbox
chosen = []
# List of names to email, transposed from the chosen list
names_to_email = []
# Dictionary associating names with their corresponding email addresses
name_dict = {}

def sendEmails(username, password, message_file):
    """
        sendEmails: takes in a Gmail username (including '@gmail.com'),
        the user's password, and the file from which to parse the message
    """

    # Email subject line
    subject = "You've Got Mail!"

    # Parse message file to create an HTML email body
    message_lines = []
    f = open(message_file, "r")
    message_lines.extend(f.readlines())
    message = "\r\n".join(message_lines)

    # Login to Gmail's SMTP server
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.ehlo()
    session.starttls()
    session.login(username, password)

    # Create email header, attach message body and send to recipient
    for name in names_to_email:
        headers = "\r\n".join(["from: " + username,
            "subject: " + subject,
            "to: " + name_dict[name],
            "mime-version: 1.0",
            "content-type: text/html"])

        content = headers + "\r\n\r\n" + message
        session.sendmail(username, name_dict[name], content)

def generateList(names):
    """
        generateList: takes in a list of names from which to generate
        a Listbox GUI using Tkinter
    """
    # Initialize Listbox to take in multiple input
    master = Tk()
    listbox = Listbox(master, selectmode = MULTIPLE, height=30, width=30)
    listbox.pack()

    # Populate Listbox with names from name list
    for name in names:
        listbox.insert(END, name)

    def callback(root):
        """
            callback: takes in user input, records it, and
            destroys the Listbox
        """
        items = map(int, listbox.curselection())
        if(len(items) == 0):
            print "No items"
        else:
            chosen.extend(items)

        root.destroy()

    # Call callback from button press, keeps Listbox active until destroyed
    button = Button(master, text = "select",
            command=lambda root=master:callback(root))
    button.pack()
    mainloop()

def buildDictFromFile(filename):
    """
        buildDictFromFile: takes in a file of names, populates
        the 'names' and 'email_addresses' lists, and builds a
        dictionary from the two
    """
    words = []

    # Open the name file for reading
    name_file = open(filename, "r")

    # Populate the 'words' list with names and email addresses
    for line in name_file:
        templine = line.split(",")
        for item in templine:
            words.append(item.strip('\n'))

    # Deal with (trivially and ineffiently) with blank lines
    for word in words:
        if word == "":
            words.remove(word)

    # Populate the email_addresses and names lists
    for word in words:
        if '@' in word:
            email_addresses.append(word)
        else:
            names.append(word)

if __name__ == '__main__':
    print "Welcome to the simple email sender!"
    print "Usage: python <name_file> <username> <password> <message_file>"
    print "Note: The name file should be comma-separated."

    # Check for valid number of command line arguments
    if len(sys.argv) < 4:
        print "Error: Usage is listed above."
        exit(1)

    # Build the dictionary, and generate the Listbox
    buildDictFromFile(sys.argv[1])
    generateList(names)

    # Actually build the dictionary
    name_dict = dict(zip(names, email_addresses))

    # Populate names of individuals to be emailed
    for item in chosen:
        names_to_email.append(names[item])

    # Print names and email addresses to contact (Primarily for debugging)
    for name in names_to_email:
        print name + ": " + name_dict[name]

    # Send emails
    sendEmails(sys.argv[2], sys.argv[3], sys.argv[4])
