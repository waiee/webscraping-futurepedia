from bs4 import BeautifulSoup 
import requests

#get html text
html_text =  requests.get('https://www.futurepedia.io').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('div', class_ = 'MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12 MuiGrid-grid-sm-6 MuiGrid-grid-md-4 MuiGrid-grid-lg-4 css-12y6uts')
print(jobs)
