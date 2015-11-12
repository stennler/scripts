import  smtplib
import getpass
import requests

r = requests.get("http://api.openweathermap.org/data/2.5/weather?q=San%20Francisco,%20CA&appid=bd82977b86bf27fb59a04b61b657fb6f")


weather = r.text
textMessage = "Weather today: " + str(weather["main"]["temp"]-270) + " degrees celsius, " + weather["weather"]["description"]

# Config Parameters
email = "zFleischman@gmail.com"
phone = "4156968432"
phoneCarrierDomain = "vtext.com"
phoneEmailAddress = phone + "@" + phoneCarrierDomain

# Get user input
password = getpass.getpass("Enter password for \"" + email + "\": ")

# Setup the smtplib to use gmail's smtp server and the given login info.
server = smtplib.SMTP( "smtp.gmail.com", 587 )
server.starttls()
server.login(email, password)

# Send an email to the phone number at the given domain.
print ("")
print ("Sending the text message \"" + textMessage + "\" to " +
        phoneEmailAddress + "...")
server.sendmail(email, phoneEmailAddress, textMessage)
print ("Sent!")
