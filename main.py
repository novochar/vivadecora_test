from bs4 import BeautifulSoup
import requests

html = requests.get("https://github.com/vivadecora/desafio-backend-trabalhe-conosco/").content
soup = BeautifulSoup(html, 'html.parser')
result = soup.find_all('div', role='rowheader')
for i in result:
  print(i.prettify())