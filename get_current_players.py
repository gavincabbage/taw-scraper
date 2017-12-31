from bs4 import BeautifulSoup
from requests import get

homepage_html = get('http://taw-server.de').text
taw_homepage = BeautifulSoup(homepage_html, 'html.parser')



