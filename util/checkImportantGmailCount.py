#!/usr/bin/python

import os
try:
    import imaplib
    
    mail = imaplib.IMAP4_SSL("imap.gmail.com",993)
    mail.login("zFleischman@gmail.com", "PASSWORD")
    status, response = mail.status('[Gmail]/Important', "(UNSEEN)"); 
    unreadcount = int(response[0].split()[2].strip(').,]'))
    
    os.system("echo " + str(unreadcount) + " > .unreadMail")
    os.system("date  >> .unreadMail")
    
finally:
    mail.logout()
