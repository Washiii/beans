################################################################################################
#											       #										   #
#	This code is FREE to use and change at any moment, this code has no CopyRights and     #
#	anything like that, the only thing that i ask you is to report any erros on my github  #
#	https://github.com/Washiii/beans/issues/new if you donn't wanna report it on the       #
#	surface web you can send me a email on pr0t_n0fg4nn@secmail.com talking about the      #
#	error (and do note use my on tool against me xD). Enjoy the code :)                    #
#											       #										   #
################################################################################################

import smtplib, ssl
import sys

from random import randint
from time import sleep

from Tools.Email_Spam_Tool.msg_create import msg_create

def create_private_server_connection(host, port)

	##########################################################################
	#									 #
	#	Create a connection with a private server (if the user wants to) #
	#   Any error on this part is handled and logged. So if you have any     #
	#	problems please submit a issue. (or try to fix for yourself and  #
	#   contribute)                                                          #
	# 									 #
	##########################################################################

	global s_conneciton

	try:
		print("Creating the connection with the private server.")
		s_conneciton = smtplib.SMTP(host=host, port=port)

		if s_conneciton:
			print("Connection with private server done")
		else:
			print("An error on SMTP connection with the private server. Quiting.")
			sys.exit(0)

	except Exception as error:
		print("An error on SMTP connection with the private server. Quiting.")
		sys.exit(error)

def create_preset_server_connection()
	global s_rambler
	global s_gmail

	#Creates the gmail SMTP server connection

	try:
		print("Creating the SMTP gmail connection")
		s_gmail = smtplib.SMTP(host='smtp.gmail.com', port=587)

		if s_gmail:
			print('Conection with gmail done!!\n')

		else:
			print("An error on SMTP connection with the gmail server. Quiting.")
			sys.exit(0)

	except  Exception as e:
		print("Error on SMTP connection (gmail)")
		sys.exit(e)

	#Creates the rambler SMTP server connection


	try:
		print("Creating the SMTP rambler connection")
		s_rambler = smtplib.SMTP(host='smtp.rambler.ru', port=587)

		if s_rambler:
			print('Conection in rambler done!!\n')
			
		else:
			print("An error on SMTP connection with the rambler server. Quiting.")
			sys.exit(0)

	except  Exception as e:
		print("Error on SMTP connection (rambler): {}".format(e))
		sys.exit(0)

	#Yahoo removed.

	return True

def login(server, email, password):

	###########################################################################
	#									  #
	#	Try to log in on the gmail, rambler and private server (if exist).#
	#   Any error on this part is handled and logged. So if you have any      #
	#	problems please submit a issue. (or try to fix for yourself and   #
	#   contribute)                                                           #
	# 									  #
	###########################################################################

	if server == "gmail":
		if email_fail[email]:
			print("This email fail on the last log in, skiping it.")

		else:
			try:
				sleep(wait)
				s_gmail.connect(host='smtp.gmail.com', port=587)
				s_gmail.ehlo()
				s_gmail.starttls()
				s_gmail.ehlo()
				s_gmail.login(email, password)

				print("Login succefful in {}".format(email))						

			except Exception as e:
				print("Fail on login in {}. Error: {}".format(email, e))
				email_fail.append(email)
				pass

	elif server == "rambler":
		if email_fail[email]:
			print("This email fail on the last log in, skiping it.")

		else:
			try:
				s_rambler.connect(host='smtp.rambler.ru', port=587)
				s_rambler.ehlo()
				s_rambler.starttls()
				s_rambler.ehlo()
				s_rambler.login(email, password)

				print("Login succefful in {}".format(email))

			except Exception as e:
				print("Fail on login in {} because {}".format(email, e))
				email_fail.append(email)
				pass

	elif sever == "private":
		if email_fail[email]:
			print("This email fail on the last log in, skiping it.")

		else:

			#You maybe need to change this lines according to your server specs

			try:
				s_conneciton.connect(host = private_host, port = private_port)
				s_conneciton.ehlo()												#You can comment this and the bottom 2 lines if your server do not use tls encryption
				s_conneciton.starttls()
				s_conneciton.ehlo()
				if private_need_login == True:
					s_conneciton.login(email, password)

				print("Login succefful in {}".format(email))

			except Exception as e:
				print("Fail on login in {} because {}".format(email, e))
				email_fail.append(email)
				pass

	#Yahoo removed

	else:
		print("An internal error on the code happened. At the 'login' function, please report this issue on the github (https://github.com/Washiii/beans/issues/new)")

	return True


def send_email(email_from = email, email_to, service):
	text = msg_create(email_from, email_to, body, load_image, image_names, subject)

	if service == "gmail":
		try:
			for attempt in range(0, 500):
				s_gmail.sendmail(email_from, email_to, text)				#Try to send the email  (500 per email)

		except Exception as e:
			error = str(e)tolower()

			if error.find('spam') >= 0:
				print("Unable to send email from '{}'. Spam detected from Gmail server.".format(email_from))
				pass

			else:
				print(e)

	elif service == "rambler":
		try:
			for attempt in range(0, 500):
				s_rambler.sendmail(email_from, email_to, text)					#Try to send the email  (500 per email)

		except Exception as e:
			error = str(e).tolower()

			if error.find('spam') >= 0:
				print("Unable to send email from '{}'. Spam detected from Rambler server.".format(email_from))
				pass

			else:
				print(e)

	elif service == "private":
		try:
			for attempt in range (0, private_max_trys):
				s_conneciton.sendmail(email_from, email_to, text)

		except Exception as e:
			error str(e)tolower()

			if error.find('spam') >= 0:
				print("Unable to send email from '{}'. Spam detected from Private server.".format(email_from))

	else:
		print("An internal error on the code happened. At the 'send_email' function, please report this issue on the github (https://github.com/Washiii/beans/issues/new)")





#TODO: verify emails domain;
#get_contacts function (both to and from)
#the "questions" parts to define variables like 'load_images' 'subject' and etc
#main function
