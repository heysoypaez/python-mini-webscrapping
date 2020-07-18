from src.render_product import render_product
from src.extract_product import *
from src.write_product_on_file import *
from src.write_headers_on_file import *

def build_product(product,file_markdown,file_csv):
	try:
		write_headers_on_file(file_csv)
		product = extract_product(product)
		render_product(product,file_markdown)
		write_product_on_file(product,file_csv)
		return True
	except Exception as e:
		print(e)