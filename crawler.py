from urllib.request import urlopen
from bs4 import BeautifulSoup

with urlopen('https://stackoverflow.com/questions') as response:
    soup = BeautifulSoup(response, 'html.parser')
    for anchor in soup.find_all('a'):
        print(anchor.get('href', '/'))
