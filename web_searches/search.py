import os
from dotenv import load_dotenv
from metaphor_python import Metaphor
import json 
from .utils import fill_prompt, prompt_chatgpt
import openai
import yaml
from pathlib import Path
from typing import Tuple, Dict, List

# Load all the environ variables
load_dotenv(dotenv_path="../.env")
METAPHOR_API_KEY = os.getenv("METAPHOR_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

PROMPT_FILE_TEMPLATE = Path("./web_searches/prompts/extract_content.prompt")

client = Metaphor(api_key=METAPHOR_API_KEY)


def return_relevant_results(unknowns: list) -> Tuple[Dict, Dict]:
     
    info_sources = {unknown: [] for unknown in unknowns} 
    info_contents = {unknown: [] for unknown in unknowns}

    for unknown in unknowns:
        # Get the relevant information for the client 
        response = client.search(unknown,
            num_results=7,
        )
 
        ids = []
        for result in response.results:
            print(result.title, result.url, "id = ", result.id)
            ids.append(result.id)
            info_sources[unknown].append(
                {
                    "url": result.url,
                    "title": result.title
                }
            )
        
        print("Got responses for our unknowns")

        all_contents = client.get_contents(ids)
        for content in all_contents.contents:

            query_prompt = fill_prompt(PROMPT_FILE_TEMPLATE, prompt=content.extract) 
            content_cleaned = prompt_chatgpt(query_prompt)
            info_contents[unknown].append(
                {
                    "url": content.url,
                    "title": content.title,
                    "extract": content_cleaned 
                }
            )
        print("Got content for our unknowns")

    return info_sources, info_contents
