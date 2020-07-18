from render_decoration import *
from build_product import *
from get_page_html_raw import *
from send_filecontent_to_gmail import send_filecontent_to_gmail

render_decoration("Starting")

# Get page html raw and grabs each notebook container from this html.
data = get_page_html_raw("https://www.solotodo.cl/notebooks")
notebooks = data.findAll("div",{"class": "category-browse-result"})

# Create files for save data notebook data received
file_csv = open("./build/notebooks.csv", "w")
file_markdown = open("./build/notebooks.md", "w")

for notebook in notebooks:
	build_product(notebook,file_markdown,file_csv)

# Close files
file_csv.close()
file_markdown.close()

# Send Email with data updated
send_filecontent_to_gmail(\
  './build/notebooks.md',\
  "Notebooks en menos de $300.000 pesos",\
  "Daniel <danielpaezsw66@gmail.com>",\
  "Daniel <danielpaezsw66@gmail.com>"\
)
