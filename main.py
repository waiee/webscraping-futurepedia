from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.futurepedia.io').text
soup = BeautifulSoup(html_text, 'html.parser')

#find all cards
cards = soup.find_all('div', class_='flex flex-col items-start')

#find all links
links = soup.find_all('div', class_='px-6 mt-auto flex items-center justify-between pb-4')

#find all desc
descs = soup.find_all('div', class_="px-6")

# Extract and print AI tools name and link
for card, link, desc in zip(cards, links, descs):
    ai_name = card.p.text
    button_link = link.span.text.strip()
    ai_link = link.find('a')['href']
    ai_desc = desc.p.text

    if button_link == "Get Deal":
        print("AI Tools Name: ", ai_name)
        print("Get Deal: ", ai_link)
        print("Description: ", ai_desc )
    else:
        print("AI Tools Name: ", ai_name)
        print("Visit Website: ", ai_link)
        print("Description: ", ai_desc )
    print(" ")

