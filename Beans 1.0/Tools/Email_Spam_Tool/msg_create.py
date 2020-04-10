import sys

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def msg_create(emailb, email_to, rand, body):
	msg = MIMEMultipart()

	msg['From'] = emailb									#Add "From" on email
	msg['To'] = email_to									#Add "To" on email
	msg['Subject'] = 'Good Morning %s'%(rand)
	msg.attach(MIMEText(body, "plain"))						#Attach the body on email

	filename = ['image0.png','image1.png','image2.png']
	for i in range(len(filename)):
		try:
			with open('Tools/Email_Spam_Tool/'+filename[i], "rb") as attachment:			#Try to open the image
				part = MIMEBase("application", "octet-stream")
				part.set_payload(attachment.read())
				encoders.encode_base64(part)						#Encode the image
				part.add_header(
					"Content-Dsposition",
					f"attachment; filename= {filename[i]}",
				)
				msg.attach(part)									#Attach the image


		except Exception as error:
			print("Erro on image load: {}\n".format(error))
			return error			
			sys.exit(0)

	text = msg.as_string()
	return text												#Return the email as text
			

if __name__ == '__main__':
	print('You need to use that as module and not as main archive')
	sys.exit(0)
