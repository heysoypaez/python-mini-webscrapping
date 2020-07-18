def render_product(product,file):
	file.write(line + "\n")
	print(line)
	for attribute,value in product.items():
		if int(product["price"]) < 300000:
			line_content = attribute + ": " + value + "\n"
			print(line_content)
			file.write(line_content)
	print(line)
	file.write(line + "\n")
