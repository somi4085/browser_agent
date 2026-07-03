from playwright.async_api import async_playwright
import base64
import os
from pathlib import Path


class BrowserController:
    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None

    async def start(self):
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(headless=False)
        self.page = await self.browser.new_page()

    async def take_screenshot(self, filename:str):
        Path("screenshots/").mkdir(exist_ok=True)
        path = f"screenshots/{filename}"
        await self.page.screenshot(path=path)
        return path
    
    async def navigate(self, url:str):
        await self.page.goto(url)


    async def get_page_content(self):
        return await self.page.content()
    
    async def get_dom_elements(self):
        result = await self.page.evaluate(
            '''() => {
                const elements = document.querySelectorAll("button, a, input, select");
                return Array.from(elements).map(el => ({
                    tag: el.tagName,
                    text: el.innerText,
                    id: el.id
                }));
            }'''
        )
        return result




