# import dependancies
from bs4 import BeautifulSoup as bs
import requests
import re



# ask the user what they would liek to know
topic = input("Hello, what would you like me to tell you about? ")

print(f"Okay, I will search for {topic}")

#save topic as a url
url = (f'https://en.wikipedia.org/wiki/{topic}')

#grab the web page
response = requests.get(url)

soup = bs(response.text, 'lxml').text
#div = soup.find('div', class_='mw-parser-output')
#p = div.find('p')

#content = soup.find('main', {'id': 'content'}).find_all('p')

text = []
#CLEANR = re.compile('<.*?>') 

#for p in content:
    #clean_p = re.sub(CLEANR,'', p)
    #text.append(p)


#clean_text = re.sub(r'<.*?>','', joined_text)

print(soup)