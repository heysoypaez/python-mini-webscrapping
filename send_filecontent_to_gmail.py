import smtplib , getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os import environ as env
from dotenv import load_dotenv
from render_decoration import render_decoration as render
load_dotenv()


def get_gmail_verified_account(user, password):

	try:
		# Host y puerto SMTP de Gmail 
		gmail = smtplib.SMTP("smtp.gmail.com" , 587)

		# Protocolo de cifrado de datos
		gmail.starttls()

		# Credenciales
		gmail.login(user,password)

		# Muestra la depuración de la operación de envio 1=true
		gmail.set_debuglevel(1)
		render("Account verified")
		return gmail
	
	except Exception as e:
		raise e


def send_filecontent_to_gmail(file_name,subject,sender, receiver):

	try:
		gmail = get_gmail_verified_account(env.get("user"),env.get("password"))

		with open(file_name, 'r') as file:
  			notebook_markdown = file.read()
  	
  	#Content-type text or htnl
		message = MIMEText(notebook_markdown, "plain") 
	
		# Email Headers
		header = MIMEMultipart()
		header["Subject"] = subject
		header["From"] = sender
		header["To"] = receiver
		header.attach(message)

		# Send Email
		gmail.sendmail(sender, receiver, header.as_string())

		# Close SMTP connection
		gmail.quit()
		render("Email Sent")
		return True

	except Exception as e:
		raise e






