from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

# Opening connection, grabbing the page raw HTML
def get_page_html_raw(url):
	try:
		uClient = uReq(url)
		page_html = uClient.read()
		uClient.close()
		# HTML parsing
		page_soup = soup(page_html,"html.parser")
		return page_soup

	except Exception as e:
		print(e)
		return ""
