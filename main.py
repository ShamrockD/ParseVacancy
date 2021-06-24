import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

from config import DRIVER_PATH, URL

# url = input()
base_url = URL
fake_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:89.0) Gecko/20100101 Firefox/89.0'}

response = requests.get(base_url, headers=fake_headers)
check_response_code = response.status_code
print(check_response_code)
response = response.text

list_of_pages = []


# Узнаем количество страниц

def get_pages_count():
    bs4_soup = BeautifulSoup(response, 'lxml')

    pages_group = bs4_soup.find('span', 'bloko-button-group')
    if pages_group:
        pagination_spans = pages_group.find('a', 'bloko-button')
        pages_count = pagination_spans.find_next().get_text()

        return int(pages_count)
    else:
        return 100


def parse_list(pages_count):
    # print(pages_count)
    for page_number in range(0, pages_count + 1):
        page_url = base_url + str(f'&page={page_number}')
        # print(page_url)
        list_of_pages.append(page_url)


def parse_vacancy():
    counter = 0
    for url in list_of_pages:
        new_url = list_of_pages[counter]
        print(new_url)
        response_for_vacancy = requests.get(new_url, headers=fake_headers).text
        vacancy_soup = BeautifulSoup(response_for_vacancy, 'lxml')
        list_vacancy_soup = vacancy_soup.find_all('div', 'vacancy-serp-item')
        counter += 1
        for item in list_vacancy_soup:
            title = item.find('span', 'g-user-content').get_text()
            print(title)
            print(counter)


if check_response_code == 200:
    number_of_pages = get_pages_count()
    if number_of_pages >= 0:
        parse_list(number_of_pages)
        print(len(list_of_pages))
        parse_vacancy()
    else:
        print('Обнаружена только одна страница')
