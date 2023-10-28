import PyPDF4
from googlesearch import search
import requests
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
from prompts import SEARCH_TABLE_OF_CONTENTS, EXTRACT_QUESTION
from pdfminer.high_level import extract_text
import re
import pdfreader
import os
from dotenv import load_dotenv
import sys

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
    return text

def search_table_of_contents(excerpt, section):
    completion = anthropic.completions.create(
        model="claude-2",
        max_tokens_to_sample=1000,
        prompt=f"{HUMAN_PROMPT} {SEARCH_TABLE_OF_CONTENTS} <excerpt>{excerpt}<excerpt> <section>{section}<section> {AI_PROMPT}",
    )
    return completion.completion

def extract_section_pages(pdf_path, start_page, limit_pages=10):
    text = extract_text(pdf_path, page_numbers=list(range(start_page, start_page + limit_pages)))
    return text

def extract_question(excerpt, question):
    completion = anthropic.completions.create(
        model="claude-2",
        max_tokens_to_sample=1000,
        prompt=f"{HUMAN_PROMPT} {EXTRACT_QUESTION} <excerpt>{excerpt}<excerpt> <question>{question}<question> {AI_PROMPT}",
    )
    return completion.completion


textbook_name = "John A. Rice, Third Edition."
# textbook_name  = "The Elements of Statistical Learning: Data Mining, Inference, and Prediction by Trevor Hastie, Robert Tibshirani, and Jerome Friedman."
chapter = "8"
section = "10"
question = "21."

# link = find_textbook_link(textbook_name)
# generate_textbook_pdf(link)

pdf_path = "downloaded_textbook.pdf"
section_title = f"8.10"
excerpt = extract_pages(pdf_path)
page_text = search_table_of_contents(excerpt, section_title)

# text = "Based on the provided excerpt and section number, the page number containing Section 8.10 is 312."
match = re.search(r"(\b\d+\b)(?!.*\b\d+\b)", page_text)
page = 312
try:
    page = int(match.group(1))
except AttributeError:
    page = 312


output = extract_section_pages(pdf_path, page)
question_content = extract_question(output, question)

# print(output)
print(question_content)


