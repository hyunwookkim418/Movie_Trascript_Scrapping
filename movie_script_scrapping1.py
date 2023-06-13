#"How to Scrape Multiple Web Pages Using Python" by Shittu Olumide
#https://www.freecodecamp.org/news/how-to-scrape-multiple-web-pages-using-python/
#How to Scrape a Single Web Page

import requests
from bs4 import BeautifulSoup

website = 'https://subslikescript.com/movie/Titanic-120338'

result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'html.parser')

box = soup.find('article', class_='main-article')
title = box.find('h1').get_text()
transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

with open(f'{title}.txt', 'w', encoding='utf-8') as file:
    file.write(transcript)
