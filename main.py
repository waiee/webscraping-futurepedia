from bs4 import BeautifulSoup 
import requests

#get website link
html_text =  requests.get('https://www.futurepedia.io')
print(html_text)
 

