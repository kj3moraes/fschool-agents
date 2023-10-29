import asyncio
import time
from googlesearch import search
import pyperclip  # handy cross-platform clipboard text handler
import wget
from serpapi import GoogleSearch
from bs4 import BeautifulSoup
import requests
import os
import format_questions
import json
import pyautogui


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

def find_assignments_page(course_code):
    # query = "MIT opencourseware course code " + str(course_code) + ". assignments page site:mit.edu"
    query = "MIT opencourseware https://ocw.mit.edu/courses/ \"" + str(course_code) + "\" assignments page"
    resp = metaphor_search(query).results
    print(resp)
    all_urls = [item.url for item in resp]
    for url in all_urls:
        if(url.endswith("pages/assignments/")):
            return url
    return "unknown"

def find_assignments_page_with_serp(course_code):
    apiKey = "367c7199e7d9478eb8f29b1a3e3f15b3c143ae053729d0a6ec5caabdf4e8073d"
    query = "site:mit.edu MIT opencourseware course code " + str(course_code) + " assignments page"
    # query = "MIT opencourseware course code " + str(course_code) + " name"
    requests.get("https://serpapi.com/search?q=")

    params = {
        "q": query,
        "location": "Austin, Texas, United States",
        "hl": "en",
        "gl": "us",
        "google_domain": "google.com",
        "api_key": apiKey,
        "num": 20,
    }

    # return json.dumps(GoogleSearch(params).get_dict(), sort_keys=True, indent=4, separators=(',', ': '))
    # return GoogleSearch(params).get_dict().get("organic_search")
    res = GoogleSearch(params).get_dict().get("organic_results")
    return [p.get("link") for p in res]

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

def find_assignments_page_via_google(course_code):
    query = "assignment page for MIT opencourseware course code " + str(course_code) + "  site:mit.edu"
    links = list(search(query, num=1, stop=1, pause=2))
    for url in links:
        if(url.endswith("pages/assignments/")):
            return url
        
def find_assignments_page_via_google2(course_code):
    # query = "assignment page for MIT opencourseware course code pages/assignments/ " + str(course_code) + "  site:mit.edu"
    query = "assignments page for course " + str(course_code) + " site:ocw.mit.edu"
    pyautogui.keyDown('command')
    pyautogui.press('space')
    pyautogui.keyUp('command')
    pyautogui.keyUp('Fn') # so we don't press the emoji bar
    pyautogui.typewrite("https://www.google.com/")
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.keyUp('Fn') # so we don't press the emoji bar
    pyautogui.typewrite(query)
    pyautogui.press('enter')
    time.sleep(2)

    # find the result on google
    pyautogui.keyDown('command')
    pyautogui.press('f')
    pyautogui.keyUp('command')
    page_query = "pages › assignments"
    pyautogui.keyUp('Fn') # so we don't press the emoji bar
    pyautogui.typewrite(page_query)
    pyautogui.press('enter')
    pyautogui.press('escape')
    pyautogui.press('tab')
    pyautogui.keyDown('shift') # get to the link
    pyautogui.press('tab')
    pyautogui.keyUp('shift')

    # pyautogui.press('tab', presses=21)
    pyautogui.press('enter') # go to the link

    pyautogui.keyDown('command')
    pyautogui.press('l')
    pyautogui.press('c')
    pyautogui.keyUp('command')
    time.sleep(1)

    return pyperclip.paste()

    

def look_for_information(assignment_num, course_code):
    # # we need to import this after we use our openai key
    # from handkerchief import Handkerchief
    # assignments_page = find_assignments_page(course_code)
    assignments_page = find_assignments_page_via_google2(course_code)
    print("assignments_page", assignments_page)
    # urls = extract_all_urls(assignments_page)
    page_text = extract_page_text(assignments_page)
    # print("page_text", page_text)
    assignment_url_raw = format_questions.get_completion("find the url that is for assignment " + str(assignment_num), page_text)
    assignment_url = requests.compat.urljoin(assignments_page, assignment_url_raw)
    print("assignment_url", assignment_url)
    download_url = get_download_url(assignment_url)
     # Convert relative URLs to absolute URLs
    absolute_url = requests.compat.urljoin(assignment_url, download_url)
    return absolute_url

def extract_page_text(url):
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup

        # Create a BeautifulSoup object
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the element with the specified id
        course_content_section = soup.find(id='course-content-section')

        # Check if the element exists
        if course_content_section:
            # Get the HTML contents of the element
            # html_contents = course_content_section.contents
            return str(course_content_section.contents)

            # Convert the contents to a string (optional)
            html_string = course_content_section.prettify()

            # Print the HTML contents
            for content in html_contents:
                print(content)

            # Print the HTML string (optional)
            print(html_string)
        else:
            print("Element with id 'course-content-section' not found.")

    else:
        print(f"Failed to retrieve the web page. Status code: {response.status_code}")
    print("rip cant find html text")
    return "rip"

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
    if os.path.exists("./problemset.pdf"):
        os.remove("./problemset.pdf")
    wget.download(resp, "./problemset.pdf")
# asyncio.run(main())

def main2():
    print(find_assignments_page_via_google2("18.650"))

# main2()