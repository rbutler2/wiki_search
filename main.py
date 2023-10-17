# ask the user what they would liek to know
topic = input("Hello, what would you like me to tell you about? ")

print(f"Okay, I will search for information about {topic}")

# import dependancies
# note that this is done after the propt so that the user does not experiance a wait time before giving the propt
from bs4 import BeautifulSoup as bs
from langchain.chains import summarize
import requests
from transformers import AutoTokenizer, DataCollatorForSeq2Seq
from transformers.utils.dummy_pt_objects import TopKLogitsWarper
from dotenv import load_dotenv
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.utils import get_stop_words

#save topic as a url
url = (f'https://en.wikipedia.org/wiki/{topic}')

#grab the web page
response = requests.get(url)

soup = bs(response.text, 'lxml').text

parser = PlaintextParser.from_string(soup, Tokenizer("english"))

summarizer = TextRankSummarizer()

summarizer.stop_words = get_stop_words("english")

summary_length = 10

summary = summarizer(parser.document, summary_length)

for sentence in summary:
    print(sentence)
