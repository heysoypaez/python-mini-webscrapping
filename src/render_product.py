def priceIsLessThan(product, price):
	priceIsLessThan = int(product["price"]) < price
	return priceIsLessThan


def render_product(product,file, line = "-" * 20):
	file.write(line + "\n")
	print(line)
	for attribute,value in product.items():
		line_content = attribute + ": " + value 
		if priceIsLessThan(product,300000):
			print(line_content)
			file.write(line_content + "\n")
	print(line)
	file.write(line + "\n")
