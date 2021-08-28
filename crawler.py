from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

# https://stackoverflow.com/questions/tagged/amazon-web-services?tab=Unanswered
# https://stackoverflow.com/questions/tagged/amazon-web-services?tab=Votes
# https://stackoverflow.com/questions/tagged/amazon-web-services?tab=Bounties

resp = requests.get('https://stackoverflow.com/questions/tagged/amazon-web-services?tab=Newest')
if resp.status_code == 200:
    print(resp.content)

# Fetches all anchor links in page
def fetchlinks():
    with urlopen('https://stackoverflow.com/questions/tagged/amazon-web-services?tab=Newest') as response:
        soup = BeautifulSoup(response, 'html.parser')
        for anchor in soup.find_all('a'):
            print(anchor.get('href', '/'))


if __name__ == '__main__':
    print("fetch links")
