import re

def extract_product(product, notebook = {} , url_base = "https://www.solotodo.cl"):

	try:
		notebook["name"] = product.h3.a.text
		notebook["url"] = url_base + product.h3.a["href"]
		notebook["price"] = re.sub("\W","", product.findAll("div",{"class":"price"})[0].a.text)
		notebook["cpu"] = product.findAll("dl",{})[0].dd.text
		notebook["ram"] = product.find(string="RAM").find_next('dd').text
		notebook["screen"] = product.find(string="Pantalla").find_next('dd').text
		notebook["storage"] = product.find(string="Almacenamiento").find_next('dd').ul.li.text 
		notebook["video"] = product.find(string="Tarjetas de video").find_next('dd').ul.li.text 
														 
		for attribute,value in notebook.items():
			value = value.replace(",","|").strip() 

			if attribute == "screen" or attribute == "cpu":
				notebook[attribute] = value.replace("\n","")

	except Exception as e:
		raise e

	return notebook
