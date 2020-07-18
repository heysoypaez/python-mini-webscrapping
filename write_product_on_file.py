def write_product_on_file(product,file):
	for keys,value in product.items():
		file.write(value + ", ")
	file.write("\n")
