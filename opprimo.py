__author__ = 'n3tn0'
__base__='n3tn0/Opprimo:master'
__baseversion__ = '1.0.2'
__version__='ALPHA'

import smtplib
import sys
import csv


#Read list of carriers and format a dictionary object to choose email suffix from
with open('carrierdb.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('carrierdb_new.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        carriers = {rows[0]: rows[1] for rows in reader}

#Make the list of carriers uppercase to avoid conflict with user input
carriers_upper = {}
upper=''
for i in carriers:
    #upper = i.upper()
    carriers_upper[i.upper()] = carriers[i]

#Determine and format the final target address
if sys.argv[2].upper() == 'EMAIL':
    target = sys.argv[1]
else:
    target = sys.argv[1] + carriers_upper[sys.argv[2].upper()]


amount = sys.argv[3]

#READ FROM TEXT FILE IN FUTURE
user = 'crush@chariot.ml'
password = 'opprimo'
smtpserver = 'chariot.ml:25'

#Get the message to be sent
body = sys.argv[4]

#Prepare message for sending
#header = 'From: %s\n' % user
#header += 'To: %s\n' % ','.join(target_addr)
#message = header + body
server = smtplib.SMTP(smtpserver)
server.starttls()

#Login to the email server
try:
    server.login(user, password)
except smtplib.SMTPAuthenticationError:
    exit()

#Send the message
for i in range(amount):
    server.sendmail(user, target, body)

#Cleanup
server.quit()