from bs4 import BeautifulSoup 
import requests

#get html text
html_text =  requests.get('https://www.futurepedia.io').text
#define soup
soup = BeautifulSoup(html_text, 'lxml')
#find all by cards
cards = soup.find_all('div', class_="flex flex-col items-start")
links = soup.find_all('div', class_ ="px-6 mt-auto flex items-center justify-between pb-4")

#find name
for card in cards:
    ai_name = card.p.text
    print("AI Tools Name: ", ai_name)

#find button link
for link in links:
    button_link = link.span.text
    ai_link = link.get('href')

    if button_link == "Get Deal":
            print("Get Deal: ", ai_link)
    else:
        print("Visit Website: ", ai_link)
