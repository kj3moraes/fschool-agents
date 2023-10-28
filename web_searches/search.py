import os
from dotenv import load_dotenv
from metaphor_python import Metaphor

# Load all the environ variables
load_dotenv(dotenv_path="../.env")

METAPHOR_API_KEY = os.getenv("METAPHOR_API_KEY")
client = Metaphor(api_key=METAPHOR_API_KEY)

# Read the file with all the unknow information
unknown_keywords = []
file = open("unknown.txt", "r+")
while True:
    line = file.readline()
    if not line:
        break
    print(line)
    unknown_keywords.append(line)

print(unknown_keywords)

info_sources = {unknown: [] for unknown in unknown_keywords} 
info_contents = {unknown: [] for unknown in unknown_keywords}

for unknown in unknown_keywords:
    response = client.search(unknown,
        num_results=5,
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

    print(info_sources) 
    content = client.get_contents(ids)
    info_contents[unknown].append(content)
    print(content)



