#!/bin/python

import  smtplib

server = smtplib.SMTP( "smtp.gmail.com", 587 )
server.starttls()
server.login( "zfleischman@gmail.com", "PASSWORD" )

server.sendmail( 'zfleischman@gmail.com', '4156968432@vtext.com', 'Dev4 is back online' )
