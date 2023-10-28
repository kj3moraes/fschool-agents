import os
from dotenv import load_dotenv
from metaphor_python import Metaphor
import json 
import openai
import yaml
from pathlib import Path
from typing import Tuple, Dict, List

# Load all the environ variables
load_dotenv(dotenv_path="../.env")
METAPHOR_API_KEY = os.getenv("METAPHOR_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

PROMPT_FILE_TEMPLATE = Path("./prompts/extract_content.prompt")

client = Metaphor(api_key=METAPHOR_API_KEY)

def fill_prompt(prompt_file: Path, info: str):
    
    with open(prompt_file) as f:
        prompt = f.read()

    prompt.replace("{{prompt}}", info)
    return prompt

def prompt_chatgpt(prompt: str) -> str:

    response = openai.Completion.create(
        prompt=prompt,
        model="gpt-4",  
        temperature=0.6
    )
    return response.choices[0].text.strip()


def return_relevant_results(unknowns: dict) -> Tuple[Dict, Dict]:
     
    info_sources = {unknown: [] for unknown in unknown_keywords} 
    info_contents = {unknown: [] for unknown in unknown_keywords}

    for unknown in unknown:
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

        all_contents = client.get_contents(ids)
        for content in all_contents.contents:

            query_prompt = fill_prompt(PROMPT_FILE_TEMPLATE, content.extract) 
            content_cleaned = prompt_chatgpt(query_prompt)
            info_contents[unknown].append(
                {
                    "url": content.url,
                    "title": content.title,
                    "extract": content_cleaned 
                }
            )

    return info_sources, info_contents
