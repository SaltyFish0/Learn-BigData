import asyncio
from playwright.async_api import async_playwright

result = []


async def run(url, user_context):
    page = await user_context.new_page()
    await page.goto(url, wait_until='networkidle')
    name = await page.query_selector("//h2[@class='m-b-sm']")
    name = await name.inner_text()
    message = await page.query_selector("//div[@class='drama']/p")
    message = await message.inner_text()
    result.append({'name': name, 'message': message})


async def main():
    async with async_playwright() as play:
        browser_type = [play.webkit, play.chromium, play.firefox]
        browser = await browser_type[1].launch(headless=False)
        user_context = await browser.new_context()
        page = await user_context.new_page()

        await page.goto('https://ssr1.scrape.center/', wait_until='networkidle')

        list_a = await page.query_selector_all("//a[@class='name']")
        list_a = [await i.get_attribute('href') for i in list_a]
        list_a = ['https://ssr1.scrape.center' + i for i in list_a]

        task_list = [asyncio.create_task(run(i, user_context)) for i in list_a]
        await asyncio.wait(task_list)

        print(result)

asyncio.run(main())
