from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.futurepedia.io').text
soup = BeautifulSoup(html_text, 'html.parser')

#find all cards
cards = soup.find_all('div', class_='flex flex-col items-start')

#find all links
links = soup.find_all('div', class_='px-6 mt-auto flex items-center justify-between pb-4')

#find all desc

# Extract and print AI tools name and link
for card, link in zip(cards, links):
    ai_name = card.p.text
    button_link = link.span.text.strip()
    ai_link = link.find('a')['href']

    if button_link == "Get Deal":
        print("AI Tools Name: ", ai_name)
        print("Get Deal: ", ai_link)
    else:
        print("AI Tools Name: ", ai_name)
        print("Visit Website: ", ai_link)
    print(" ")

