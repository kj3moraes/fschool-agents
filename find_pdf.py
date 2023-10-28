# GPT-4 powered playwright browser for using the internet

# We use metaphor search but you can use serpAPI: https://serpapi.com/

def metaphor_search(information_to_find):
    from metaphor_python import Metaphor
    metaphor = Metaphor("b12b105b-c275-4837-b4f8-b8ae11b24501")

    response = metaphor.search(
    information_to_find,
    num_results=10,
    use_autoprompt=True,
    )

    return response


async def look_for_information(information_to_find):
    resp = metaphor_search(information_to_find).results

    from handkerchief import Handkerchief
    handkerchief = Handkerchief()

    for item in resp:
        content = await async_load_playwright(item.url)
        handkerchief.index(content)

    messages = [{'role': 'user', 'content': information_to_find}]
    response = handkerchief.sneeze(messages, model='gpt-4', stream=False)
    return response

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
    return results

look_for_information("")