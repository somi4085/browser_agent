from browser import BrowserController
import re

class ActionExecutor:

    def __init__(self,browser:BrowserController):
        self.browser = browser
    
    async def execute(self, action:str):
        if "click" in action:
            match = re.search(r'click\s(.+)',action)
            await self.browser.page.click(match.group(1))
        elif "navigate" in action:
            match = re.search(r'navigate\s(\S+)',action)
            await self.browser.navigate(match.group(1))
        elif "type" in action:
            match = re.search(r'type\s+(.+)', action)
            await self.browser.page.type(match.group(1))
        elif "screenshot" in action:
            await self.browser.take_screenshot("step.png")

    