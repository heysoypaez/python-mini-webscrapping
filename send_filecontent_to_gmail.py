import smtplib , getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def get_gmail_verified_account(user, password)

	# Host y puerto SMTP de Gmail 
	gmail = smtplib.SMTP("smtp.gmail.com" , 587)

	# Protocolo de cifrado de datos
	gmail.starttls()

	# Credenciales
	gmail.login(user,password)

	# Muestra la depuración de la operación de envio 1=true
	gmail.set_debuglevel(1)
	return gmail

def send_filecontent_to_gmail():

	gmail = get_gmail_verified_account(env.user , env.password)

	with open('notebooks.md', 'r') as file:
    notebook_markdown = file.read()

	remitente = "Daniel <danielpaezsw66@gmail.com>"
	destinatario = remitente
	mensaje = MIMEText(notebook_markdown, "plain") #Content-type text htnl

	# Email Headers
	header = MIMEMultipart()
	header["Subject"] = "Notebooks en menos de $300.000 pesos"
	header["From"] = remitente
	header["To"] = destinatario
	header.attach(mensaje)

	# Enviar
	gmail.sendmail(remitente, destinatario, header.as_string())

	# Cerrar conexion SMTP
	gmail.quit()
