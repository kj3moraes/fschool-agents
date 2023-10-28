from pathlib import Path
import re
import nltk
import openai
import os
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI

nltk.download('stopwords')
nltk.download('wordnet')

load_dotenv(".env")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def fill_prompt(prompt_file: Path, **kwargs):

    with open(prompt_file) as f:
        prompt = f.read()

    wl = WordNetLemmatizer()

    for k, v in kwargs.items():
        v = v.lower()
        cleaned_value = " ".join([wl.lemmatize(word) for word in v.split(
        ) if not word in set(stopwords.words('english'))])
        prompt = prompt.replace(f"{{{k}}}", v)

    return prompt


def prompt_chatgpt(prompt: str) -> str:

    message = [{"role":"user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=message,
        temperature=0.6,
    )
    return response.choices[0].message.content.strip()
