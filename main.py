from bs4 import BeautifulSoup 
import requests

#get html text
html_text =  requests.get('https://www.futurepedia.io').text
#define soup
soup = BeautifulSoup(html_text, 'lxml')
#find all by cards
cards = soup.find_all('div', class_="flex flex-col items-start")

for card in cards:
    ai_name = card.p.text
    print("AI Tools Name: ", ai_name)