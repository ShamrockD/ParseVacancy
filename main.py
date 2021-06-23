import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

from config import DRIVER_PATH, URL

url = input()
fake_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:89.0) Gecko/20100101 Firefox/89.0'}

response = requests.get(url, headers=fake_headers)
check_response_code = response.status_code
print(check_response_code)
response = response.text

# Узнаем количество страниц

def get_pages_count():

    bs4_soup = BeautifulSoup(response, 'lxml')

    pages_group = bs4_soup.find('span', 'bloko-button-group')
    pagination_spans = pages_group.find('a', 'bloko-button')
    pages_count = pagination_spans.find_next().get_text()

    print(f'Всего страниц для поиска {pages_count}')
    return pages_count

def


if check_response_code == 200:
    get_pages_count()
