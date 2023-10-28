from web_searches import retrieve_textbook_sections
from pathlib import Path
import json

textbook_path = Path("./textbooks/statistics.pdf")
question = "What is the chi-squared distribution?"

answers = retrieve_textbook_sections(textbook_path, question)
print(answers)
with open("answer.json", "w+") as f:
    json.dump(answers, f, indent=4)