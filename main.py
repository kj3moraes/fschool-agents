
import requests
from bs4 import BeautifulSoup
from fpdf import FPDF
import os
from dotenv import load_dotenv
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
from prompts import SUMMARIZE_QUESTION


load_dotenv()

CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")
anthropic = Anthropic(api_key=CLAUDE_API_KEY)
