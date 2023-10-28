from pathlib import Path
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download('stopwords')
nltk.download('wordnet')

def fill_prompt(prompt_file: Path, **kwargs):
    
    with open(prompt_file) as f:
        prompt = f.read()

    for k, v in kwargs.items(): 
        prompt = prompt.replace(f"{{{k}}}", v)
    
    # Cleaning the prompt
    prompt = prompt.lower()
    prompt = re.sub(r"(@\[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?", "", prompt)
    cleaned_prompt = [wl.lemmatize(word) for word in prompt.split() if not word in set(stopwords.words('english'))]
    return cleaned_prompt

