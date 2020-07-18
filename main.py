import re
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import smtplib , getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



line = "---------------------------------------------"
url_base = "https://www.solotodo.cl"
url = "https://www.solotodo.cl/notebooks"

# Opening connection, grabbing the page
uClient = uReq(url)
page_html = uClient.read()
uClient.close()

# HTML parsing
page_soup = soup(page_html,"html.parser")

# Grabs each notebook
notebooks = page_soup.findAll("div",{"class": "category-browse-result"})

# Create a file
filename = "notebooks.csv"
f = open(filename, "w")

filename_2 = "notebooks.md"
f_2 = open(filename_2, "w")

def extract_product(product):
	notebook = {}
	notebook["name"] = product.h3.a.text
	notebook["url"] = url_base + product.h3.a["href"]
	notebook["price"] = re.sub("\W","", product.findAll("div",{"class":"price"})[0].a.text)

	notebook["cpu"] = product.findAll("dl",{})[0].dd.text \
													 .replace("\n","")

	notebook["ram"] = product.find(string="RAM") \
													 .find_next('dd').text

	notebook["screen"] = product.find(string="Pantalla") \
															.find_next('dd').text \
															.replace("\n","")
	
	notebook["storage"] = product.find(string="Almacenamiento") \
															 .find_next('dd').ul.li.text 

	notebook["video"] = product.find(string="Tarjetas de video") \
														 .find_next('dd').ul.li.text 
														 
	for attribute,value in notebook.items():
		notebook[attribute] = value.replace(",","|") \
															 .strip() 

	return notebook

def render_product(product):
	f_2.write(line + "\n")
	print(line)
	for attribute,value in product.items():
		if int(product["price"]) < 300000:
			line_content = attribute + ": " + value + "\n"
			print(line_content)
			f_2.write(line_content)
	print(line)
	f_2.write(line + "\n")

def write_product_on_file(product):
	for headers,value in product.items():
		f.write(value + ", ")
	f.write("\n")

def write_headers_on_file():
	f.write("name, url, price, cpu, ram, screen, storage, video \n")

def render():
	print(line)
	print("Starting")
	print(line)
	return True

def build_product(product):
	product = extract_product(product)
	render_product(product)
	write_product_on_file(product)
	return True

render()
write_headers_on_file()
for notebook in notebooks:
	build_product(notebook)

# Cierres
f_2.close()
f.close()


user = "danielpaezsw66@gmail.com"
password = "google1r2a3s"

# Email Headers
##remitente = input("From, ejemplo: administrador <admin@gmail.com>: ")
remitente = "Daniel <danielpaezsw66@gmail.com>"
##destinatario = input("To, ejemplo: administrador <admin@gmail.com>: ")
destinatario = remitente
##asunto = input("Subject, Asunto del mensaje: ")

with open('notebooks.md', 'r') as file:
    notebook_markdown = file.read()

# str = open('very_Important.txt', 'r').read()

mensaje = notebook_markdown

# Host y puerto SMTP de Gmail 
gmail = smtplib.SMTP("smtp.gmail.com" , 587)

# Protocolo de cifrado de datos
gmail.starttls()

# Credenciales
gmail.login(user,password)

# Muestra la depuración de la operación de envio 1=true
gmail.set_debuglevel(1)

header = MIMEMultipart()
header["Subject"] = "Notebooks en menos de $300.000 pesos"
header["From"] = remitente
header["To"] = destinatario
mensaje = MIMEText(mensaje, "plain") #Content-type text htnl
header.attach(mensaje)

# Enviar
gmail.sendmail(remitente, destinatario, header.as_string())

# Cerrar conexion SMTP
gmail.quit()
