from render_decoration import *
from build_product import *
from get_page_html_raw import *
render_decoration("Starting")

# Get page html raw and grabs each notebook container from this html.
data = get_page_html_raw("https://www.solotodo.cl/notebooks")
notebooks = data.findAll("div",{"class": "category-browse-result"})

# Create files for save data notebook data received
file_csv = open("notebooks.csv", "w")
file_markdown = open("notebooks.md", "w")

for notebook in notebooks:
	build_product(notebook,file_markdown,file_csv)

# Close files
file_csv.close()
file_markdown.close()