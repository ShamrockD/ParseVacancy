import lxml
import requests
from bs4 import BeautifulSoup

url = input()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:89.0) Gecko/20100101 Firefox/89.0'}

response = requests.get(url, headers=headers)
check_response_code = response.status_code

print(check_response_code)
