from bs4 import BeautifulSoup 
import requests

#get html text
html_text =  requests.get('https://www.futurepedia.io').text

#define soup
soup = BeautifulSoup(html_text, 'lxml')
ai = soup.find('div', class_ = 'MuiBox-root css-a0wou3')
ai_name = ai.find('h3', class_='MuiTypography-root MuiTypography-h6 MuiTypography-alignLeft css-nxqa8p')
print(ai_name)