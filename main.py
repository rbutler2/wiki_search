# ask the user what they would liek to know
topic = input("Hello, what would you like me to tell you about? ")

print(f"Okay, I will search for information about {topic}")

# import dependancies
# note that this is done after the propt so that the user does not experiance a wait time before giving the propt
from bs4 import BeautifulSoup as bs
import requests
from transformers import AutoTokenizer, DataCollatorForSeq2Seq
from transformers.utils.dummy_pt_objects import TopKLogitsWarper
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import WebBaseLoader
from langchain.chains.summarize import load_summarize_chain
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
import openai

#save topic as a url
url = (f'https://en.wikipedia.org/wiki/{topic}')

#grab the web page
response = requests.get(url)

soup = bs(response.text, 'lxml').text

#import api key
keys_file = open("config.txt")
lines = keys_file.readlines()
api_key = lines[0].rstrip()
openai.api_key = api_key

#define the propt
propt_template = """please summerize the following: "{soup}" CONCISE SUMMARY:"""

propt = PromptTemplate.from_template(propt_template)

#define llm chain
llm = ChatOpenAI(tempature=0, model_name="gpt-3.5-turbo-16k")
llm_chain = LLMChain(llm=llm, propt=propt)

#define stuff documant chain
stuff_chain = StuffDocumentsChain(
    llm_chain=llm_chain, document_variable_name="soup"
)

docs = loader.load()
print(stuff_chain.run(docs))

# tokenizer = AutoTokenizer.from_pretrained(soup)

# prefix = "summarize: "

# def preprocess_function(input):
#     inputs = [prefix + doc for doc in input["text"]]
#     model_inputs = tokenizer(inputs, max_length=1024, truncation=True)

#     labels = tokenizer(text_target=input["summary"], max_length=128, truncation=True)

#     model_inputs["labels"] = labels["input_ids"]
#     return model_inputs


# data_collator = DataCollatorForSeq2Seq(tokenizer=tokenizer, model=soup, return_tensor="tf")


# print(tokenizer)