from googlesearch import search
import requests
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
from prompts import SEARCH_TABLE_OF_CONTENTS
from pdfminer.high_level import extract_text
import re
import pdfreader
import os
from dotenv import load_dotenv

load_dotenv()

CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")
anthropic = Anthropic(api_key=CLAUDE_API_KEY)

def find_textbook_link(textbook_name):
    query = textbook_name + " PDF"
    links = list(search(query, num=1, stop=1, pause=2))
    
    if links:
        return links[0]
    else:
        return None

def generate_textbook_pdf(link):
    response = requests.get(link)
    response.raise_for_status()

    with open("downloaded_textbook.pdf", "wb") as f:
        f.write(response.content)

    # Extract text using PdfReader
    text = extract_text("downloaded_textbook.pdf")


def extract_pages(pdf_path, limit_pages=10):
    text = extract_text(pdf_path, page_numbers=list(range(limit_pages)))
    print(text)
    return text

def search_table_of_contents(excerpt, section):
    completion = anthropic.completions.create(
        model="claude-2",
        max_tokens_to_sample=1000,
        prompt=f"{HUMAN_PROMPT} {SEARCH_TABLE_OF_CONTENTS} <excerpt>{excerpt}<excerpt> <section>{section}<section> {AI_PROMPT}",
    )
    print(completion.completion)


textbook_name = "John A. Rice, Third Edition."
# textbook_name  = "The Elements of Statistical Learning: Data Mining, Inference, and Prediction by Trevor Hastie, Robert Tibshirani, and Jerome Friedman."
chapter = "8"
section = "10"
# chapter = "8"
# section = "10"
# problem = "21"

# link = find_textbook_link(textbook_name)
# generate_textbook_pdf(link)

pdf_path = "downloaded_textbook.pdf"
section_title = f"8.10"
excerpt = extract_pages(pdf_path)
page = search_table_of_contents(excerpt, section_title)

print(page)
# if page:
#     print(f"Section {section_title} is found on page {page}.")
# else:
#     print(f"Section {section_title} was not found in the first 25 pages.")

# link = find_textbook_link("John A. Rice, Third Edition.")
# generate_textbook_pdf(link)
# file_path = "downloaded_textbook.pdf"
# excerpt = extract_text_from_pdf(file_path)
# result = search_table_of_contents(excerpt, f"{chapter}.{section}")

# print(excerpt)
# print(result)
