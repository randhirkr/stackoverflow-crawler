from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

# https://stackoverflow.com/questions/tagged/amazon-web-services?tab=Unanswered
# https://stackoverflow.com/questions/tagged/amazon-web-services?tab=Votes
# https://stackoverflow.com/questions/tagged/amazon-web-services?tab=Bounties

response = requests.get('https://stackoverflow.com/questions/tagged/amazon-web-services?tab=Newest')
if response.status_code == 200:
    page_content = BeautifulSoup(response.content, 'html.parser')
    question_list = page_content.find_all(class_='question-summary')
    # print(question_list)
    for question in question_list:
        topic = question.find(class_='question-hyperlink').get_text()
        print(topic)
        url = question.find(class_='question-hyperlink').get('href', '/')
        print("https://stackoverflow.com"+url)
        print()


# Fetches all anchor links in page
def fetchlinks():
    with urlopen('https://stackoverflow.com/questions/tagged/amazon-web-services?tab=Newest') as response:
        soup = BeautifulSoup(response, 'html.parser')
        for anchor in soup.find_all('a'):
            print(anchor.get('href', '/'))


if __name__ == '__main__':
    print("fetch links")
