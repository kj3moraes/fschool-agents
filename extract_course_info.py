from string import Formatter
from pydantic import BaseModel
from pydantic import create_model
import os
import reasoner
import openai
# os.environ["OPENAI_API_KEY"] = 
# openai.api_key = "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"#open('openai_key.txt', 'r').read().strip('\n')
os.environ["OPENAI_API_KEY"] = open('openai_key.txt', 'r').read().strip('\n')

def extract():
    reasoner = reasoner.FancyStructuredReasoner(system_prompt="DO NOT OUTPUT ANY MORE TEXT AFTER ANSWERING THE PROMPT. BE A ROBOT.", model='gpt-3.5-turbo')
    reasoner.add_message("user", "Please submit your solutions to assignment 5 from MIT opencourseware course code 3E.45")
    assignment_num = reasoner.extract_info("the assignment number is {x}", int)
    course_code = reasoner.extract_info("the course code is {x}", str)