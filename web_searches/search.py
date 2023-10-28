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

info_sources = []
for unknown in unknown_keywords:
    response = client.search("funny article about tech culture",
        num_results=5,
        include_domains=["nytimes.com", "wsj.com"],
        start_published_date="2023-06-12"
    )
    print(response)
    print(response["ID"])
    print(response["URL"])

