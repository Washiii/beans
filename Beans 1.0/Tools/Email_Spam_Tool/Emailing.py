import smtplib, ssl
import sys

from random import randint
from time import sleep

from Tools.Email_Spam_Tool.msg_create import msg_create

running = True
rand = 0


def create_crambler():
	global s_rambler

	try:				#Create the SMTP with the rambler server
		print("Creating the SMTP rambler connection")
		s_rambler = smtplib.SMTP(host='smtp.rambler.ru', port=587)
		print('Conection in rambler done!!\n')

	except  Exception as e:
		print("Error on SMTP connection (rambler): {}".format(e))		#Error detect and print
		sys.exit(0)
		
def create_cgmail():
	global s_gmail
	try:				#Create the SMTP with the gmail server
		print("Creating the SMTP gmail connection")
		s_gmail = smtplib.SMTP(host='smtp.gmail.com', port=587)
		print('Conection in gmail done!!\n')

	except  Exception as e:
		print("Error on SMTP connection (gmail): {}".format(e))			#Error detect and print
		sys.exit(0)
			
def create_cyahoo():
	global s_yahoo
	try:
		print("Creating the SMTP yahoo connection")
		s_yahoo = smtplib.SMTP(host="smtp.mail.yahoo.com", port=587)
		print("Conecition in yahoo done!!\n")

	except Exception as e:
		print("Error on SMTP connecition (yahoo): {}".format(e))
		sys.exit(0)

def login_rambler():
	try:
		sleep(wait)											#Wait the wait time
		s_rambler.connect(host='smtp.rambler.ru', port=587)
		s_rambler.ehlo()
		s_rambler.starttls()
		s_rambler.ehlo()
		s_rambler.login(emailw, passw)						#Try to login
		print("Login succefful in {}".format(emailw))		#If login sucefull print this

		try:
			for j in range(0, len(emails_to)):				#If login sucefful try to send the email
				email_to_ = emails_to[j]
				send_email_rambler(emailw, email_to_)
				sleep(wait)									#After send (or not) wait the wait time again

		except Exception as error:
			print("Error on email create or send, because: {}".format(error))
							

	except Exception as e:
		print("Fail on login in {} because {}".format(emailw, e))	#If login fails print that and continue
						
def login_gmail():
	try:
		sleep(wait)											#Same thing than rambler
		s_gmail.connect(host='smtp.gmail.com', port=587)
		s_gmail.ehlo()
		s_gmail.starttls()
		s_gmail.ehlo()
		s_gmail.login(emailw, passw)

		print("Login succefful in {}".format(emailw))
						
		try:
			for k in range(0, len(emails_to)):
				email_to_ = emails_to[k]
				send_email_gmail(emailw, email_to_)
				sleep(wait)
		except Exception as error:
			print("Error on email create or send, because: {}".format(error))
								

	except Exception as e:
		print("Fail on login in {} because {}".format(emailw, e))
		pass
						
def login_yahoo():
	try:
		sleep(wait)
		s_yahoo.connect(host="smtp.mail.yahoo.com", port=587)
		s_yahoo.ehlo()
		s_yahoo.starttls()
		s_yahoo.ehlo()
		s_yahoo.login(emailw, passw)
						
		print("Login succefful in {}".format(emailw))

		try:
			for l in range(0, lenI(emails_to)):
				email_to_ = emails_to[l]
				send_email_yahoo(emailw, email_to_)
				sleep(wait)
						
		except Exception as error:
			print("Error on email create or send, because {}".format(error))
					
	except Exception as e:
		print("Fail to login in {} because {}".format(emailw, e))
		pass
				
def open_text():
	try:
		print('Opennig the message file...')
		message = open('Tools/Email_Spam_Tool/text_message.txt', mode='r', encoding='utf-8')
		body = str(message)
		print('Done...')
		
	except Exception as e:
		print('No text message on path, do you want to conitue?')
		awnser = input('y/N: ')
		
		if awnser == 'y' or awnser == 'Y':
			pass
			
		elif awnser == '' or awnser == 'n' or awnser == 'N':
			sys.exit(0)
			
		else:
			print('Invalid awnser.')
			sys.exit(0)

def send_email_rambler(emaila, email_to):
	global rand
	text = msg_create(emaila, email_to, rand, body)					#Create the email
	

	if emaila.find('rambler') >= 0 or emaila.find("myrambler") >= 0 or emaila.find("ro.ru") >= 0:
		try:
			for a in range(0, 500):
				s_rambler.sendmail(emaila, email_to, text)					#Try to send the email  (500 per email)
				rand = rand + 1
		except Exception as e:
			error = str(e)
			if error.find('Spam') >= 0:
				print("Unable to send email from '{}'. Spam detected from Rambler server.".format(emailw))
				pass
			else:
				print(e)

def send_email_gmail(emaila, email_to):
	global rand
	text = msg_create(emaila, email_to, rand, body)					#Create the email
	

	if emaila.find('gmail') >= 0:
		try:
			for a in range(0, 500):
				s_gmail.sendmail(emaila, email_to, text)				#Try to send the email  (500 per email)
				rand = rand + 1
		except Exception as e:
			error = str(e)
			if error.find('spam') >= 0:
				print("Unable to send email from '{}'. Spam detected from Gmail server.".format(emailw))
				pass
			else:
				print(e)

def send_email_yahoo(emaila, email_to):
	global rand
	text = msg_create(emaila, email_to, rand, body)


	if emaila.find('yahoo') >= 0:
		try:
			for a in range(0, 500):
				s_yahoo.sendmail(emaila, emailto, text)
				rand = rand + 1
			
		except Exception as e:
			error = str(e)
			
			if error.find('spam') >= 0:
				print("Unable to send email from '{}'. Spam detected from Yahoo server".format(emailw))
				pass
				
			else:
				print(e)

def verify_domain(emailw):
	if emailw.find("rambler") >= 0 or emailw.find("myrambler") >= 0 or emailw.find("ro.ru") >= 0:
		return "rambler"

	elif emailw.find("gmail") >= 0:
		return "gmail"

	elif emailw.find("yahoo") >= 0:
		return "yahoo"

	else:
		return False

def login():					#Login Function
	global s_rambler
	global s_gmail
	global s_yahoo
	global emailt_to_
	global emailw
	global passw
	global running
	global wait

	print("Starting the login and sent phase...\n")
	try:
		while running:														#'Infinite' loop
			for i in range(0,len(emails)):									#For each one in emails array try to login
				emailw = emails[i]
				passw = passwords[i]
				
				wait = randint(5,7)											#Generate a random number (in between 5 and 7) to wait before do something (help agaisnt spam detect)
				
				domain = verify_domain(emailw)

				if domain == "rambler":	#Verify rambler emails domains (i think has more than that)
					login_rambler()
						
				elif domain == "gmail":								#Verify gmail domain
					login_gmail()
				
				elif domain == "yahoo":
					login_yahoo()

				elif domain == False:
					print("Unknow email service. Jumping it")
					pass
					
	except KeyboardInterrupt:
		running = False
		sys.exit(0)

def get_contacts():				#Get the emails "To" and  "From" in differents .txt files
	global emails
	global emails_to
	global passwords
	

	print('Collecting "From" Emails and Passwords...\n')
	

	emails = []
	passwords = []
	emails_to = []
	
	
	try:
		with open("Tools/Email_Spam_Tool/email_list.txt", mode='r', encoding='utf-8') as first:
			for email in first:
				emails.append(email.split()[0])
				passwords.append(email.split()[1])

				act_email = email.split()[0]

				if act_email.find("gmail") >= 0:
					print("Gmail account added")

				elif act_email.find("rambler") >= 0 or act_email.find("ro.ru") >= 0:
					print("Rambler account added")
				
				elif act_email.find("yahoo") >= 0:
					print("Yahoo account added")
				
				else:
					print("Unknow email service.")

	except Exception as error:
		print("The file doesn't exist: {}".format(error))
		sys.exit(0)


	print('Collecting "To" Emails...')
	

	try:
		with open("Tools/Email_Spam_Tool/emails_to_list.txt", mode='r', encoding='utf-8') as second:
			for emaill in second:
				emails_to.append(emaill.split()[0])
				print("{} has added!".format(email))
				
		print("Collection done...\n")

	except Exception as error:
		print("The file doesn't exist: {}".format(error))
		sys.exit(0)

	return True

def main():
	open_text()
	create_cgmail()
	create_crambler()
	create_cyahoo
	contacts_states = get_contacts()

	try:
		if contacts_states == True:
			login()
		else:
			print("A error on get contacts step make the program stop. Please make sure to check all files again.")
			sys.exit(0)
	except Exception as e:
		print("Error {}. Exiting...".format(e))
		sys.exit(0)
main()