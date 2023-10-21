# ask the user what they would liek to know
topic = input("Hello, what would you like me to tell you about? ")

print(f"Okay, I will search for information about {topic}")

email = input("To grab the information from wikipidia please tell me your email ")

# import dependancies
# note that this is done after the propt so that the user does not experiance a wait time before giving the propt
from bs4 import BeautifulSoup as bs
import requests
from dotenv import load_dotenv
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.utils import get_stop_words
import wikipediaapi

#save topic as a url
#url = (f'https://en.wikipedia.org/wiki/{topic}')

#grab the web page
#response = requests.get(url)

#soup = bs(response.text, 'lxml').text

wiki_wiki = wikipediaapi.Wikipedia(f"MyProjectName ({email})","en")

page = wiki_wiki.page(topic)

text = ()

if page.exists():
    text = page.text 
else:
    print("Sorry but this page does not exist")

#print(text)

parser = PlaintextParser.from_string(text, Tokenizer("english"))

summarizer = TextRankSummarizer()

summarizer.stop_words = get_stop_words("english")

summary_length = 20

summary = summarizer(parser.document, summary_length)

for sentence in summary:
    print(sentence)
