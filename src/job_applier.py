from browser import BrowserController
from agents import VisionAgent
from job_profile import JobProfile


class JobApplier:

    def __init__(self, browser:BrowserController, agent:VisionAgent):
        self.browser = browser
        self.agent = agent
    
    async def fill_form(self):
        screenshot = await self.browser.take_screenshot("form.png")
        fields = await self.agent.analyze_screenshots(screenshot, "Identify all form fields on this page and return them as a list")
        return fields

        
    
    async def apply_to_job(self, job_url:str):
        await self.browser.navigate(job_url)
        await self.fill_form()
