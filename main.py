from web_searches import *
from pathlib import Path
import json

textbook_path = Path("./textbooks/statistics.pdf")
questions = ["what is the chi-squared distribution?"]

unknowns = {
    "what is the chi-squared distribution?": {
        "chi-squared distribution",
        "statistics",
        "probability distributions"
    } 
}


answers = get_answers(questions, unknowns)

with open("final_answers.json","w+") as f:
    json.dump(answers, f, indent=4)