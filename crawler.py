from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

# https://stackoverflow.com/questions/tagged/amazon-web-services?tab=Unanswered
# https://stackoverflow.com/questions/tagged/amazon-web-services?tab=Votes
# https://stackoverflow.com/questions/tagged/amazon-web-services?tab=Bounties
# fetch latest question with AWS tag on stackoverflow
url = 'https://stackoverflow.com/questions/tagged/amazon-web-services?tab=Newest'
response = requests.get(url)
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
