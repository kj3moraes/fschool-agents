import asyncio
import wget
from bs4 import BeautifulSoup
import requests
import os
import format_questions

os.environ["OPENAI_API_KEY"] = open('openai_key.txt', 'r').read().strip('\n')

def metaphor_search(information_to_find):
    from metaphor_python import Metaphor
    metaphor = Metaphor("b12b105b-c275-4837-b4f8-b8ae11b24501")

    response = metaphor.search(
    information_to_find,
    num_results=10,
    use_autoprompt=True,
    )

    return response

def find_assignments_page(information_to_find):
    resp = metaphor_search(information_to_find).results
    all_urls = [item.url for item in resp]
    for url in all_urls:
        if(url.endswith("pages/assignments/")):
            return url
    return "unknown"

def extract_all_urls(url):
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    
    urls = []

    # Extract URLs from <a> tags
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']

        # Convert relative URLs to absolute URLs
        absolute_url = requests.compat.urljoin(url, href)
        urls.append(absolute_url)
    
    return urls

def get_download_url(url):
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the webpage using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all elements with class="download-file"
        download_links = soup.find_all(class_='download-file')

        # Extract and print the links
        for link in download_links:
            download_link = link.get('href')
            return download_link
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")


async def look_for_information(information_to_find):
    # # we need to import this after we use our openai key
    # from handkerchief import Handkerchief
    assignments_page = find_assignments_page(information_to_find)
    urls = extract_all_urls(assignments_page)
    # print("all urls", urls)
    assignment_url = format_questions.get_completion("in this list of urls, find the url that is the " + information_to_find, str(urls))
    download_url = get_download_url(assignment_url)
     # Convert relative URLs to absolute URLs
    absolute_url = requests.compat.urljoin(assignment_url, download_url)
    return absolute_url

async def async_load_playwright(url: str) -> str:
    """Load the specified URLs using Playwright and parse using BeautifulSoup."""
    from bs4 import BeautifulSoup
    from playwright.async_api import async_playwright

    results = ""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        try:
            page = await browser.new_page()
            await page.goto(url)

            page_source = await page.content()
            soup = BeautifulSoup(page_source, "html.parser")

            for script in soup(["script", "style"]):
                script.extract()

            text = soup.get_text()
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            results = "\n".join(chunk for chunk in chunks if chunk)
        except Exception as e:
            results = f"Error: {e}"
        await browser.close()
    print("FOUND RESULTS", results)
    return results

async def main():
    # res = asyncio.run(look_for_information("date of birth of barack obama"))
    # print(res)
    information_to_find = "pdf file link for assignment 3 from MIT opencourseware course code Hydrodynamics (13.012)"
    # resp = metaphor_search(information_to_find).results
    resp = await look_for_information(information_to_find)
    wget.download(resp, "./problemset.pdf")
asyncio.run(main())
