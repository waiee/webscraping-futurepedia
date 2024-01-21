from bs4 import BeautifulSoup 
import requests

#get html text
html_text =  requests.get('https://www.futurepedia.io').text

#define soup
soup = BeautifulSoup(html_text, 'lxml')

#find all by tag
tags = soup.find_all('h5')
print(tags)