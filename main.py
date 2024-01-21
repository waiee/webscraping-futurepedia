from bs4 import BeautifulSoup 
import requests

#get html text
html_text =  requests.get('https://www.futurepedia.io').text
#define soup
soup = BeautifulSoup(html_text, 'lxml')
#find all by cards
cards = soup.find_all('div', class_="flex flex-col items-start")
links = soup.find_all('div', class_ ="px-6 mt-auto flex items-center justify-between pb-4")

for card in cards:
    ai_name = card.p.text

    #find name
    print("AI Tools Name: ", ai_name)

    #find link
for link in links:
    button_link = card.span.text
    if button_link == "Get Deal":
            print("Get Deal: ", button_link)
    else:
        print("Visit Website: ", button_link)
