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
        await browser.c