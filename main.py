# ask the user what they would liek to know
topic = input("Hello, what would you like me to tell you about? ")

print(f"Okay, I will search for information about {topic}")

email = input("To grab the information from wikipidia please tell me your email ")

# import dependancies
# note that this is done after the propt so that the user does not experiance a wait time before giving the propt
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer
from sumy.utils import get_stop_words
import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia(f"MyProjectName ({email})","en")

page = wiki_wiki.page(topic)

text = ()

if page.exists():
    text = page.text 
else:
    print("Sorry but this page does not exist")

parser = PlaintextParser.from_string(text, Tokenizer("english"))

summarizer = TextRankSummarizer()

summarizer.stop_words = get_stop_words("english")

summary_length = input("How long would you like the summary to be? ")

if type(summary_length) is int:
    f_summary_length = summary_length 

elif summary_length == "short".lower():
    f_summary_length = 5

elif summary_length == "medium".lower():
    f_summary_length = 10

elif summary_length == "long".lower():
    f_summary_length = 20


summary = summarizer(parser.document, f_summary_length)

print(f"\n------------------------------------\n{topic}\n------------------------------------\n")
for sentence in summary:
    print(sentence)
print("\n------------------------------------\n")