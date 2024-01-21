from bs4 import BeautifulSoup 
import requests

#get html text
html_text =  requests.get('https://www.futurepedia.io').text

#define soup
soup = BeautifulSoup(html_text, 'lxml')

#find all by tag
tags = soup.find_all('div', class_='flex flex-col bg-card text-card-foreground h-full w-full rounded-xl border shadow-lg')
