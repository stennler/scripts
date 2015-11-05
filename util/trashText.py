import  smtplib
import getpass

# Config Parameters
email = "trashtrash@trashmail.com"
phone = "4156968432"
phoneCarrierDomain = "vtext.com"
phoneEmailAddress = phone + "@" + phoneCarrierDomain

# Get user input
password = getpass.getpass("Enter password for \"" + email + "\": ")
textMessage = raw_input("Enter text message: ")

# Setup the smtplib to use gmail's smtp server and the given login info.
server = smtplib.SMTP( "smtp.trashmail.net", 587 )
server.starttls()
server.login(email, password)

# Send an email to the phone number at the given domain.
print ("")
print ("Sending the text message \"" + textMessage + "\" to " +
        phoneEmailAddress + "...")
server.sendmail(email, phoneEmailAddress, textMessage)
print ("Sent!")
