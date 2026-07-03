from browser import BrowserController
from job_profile import JobProfile

class JobSearch:
    def __init__(self, browser:BrowserController):
        self.browser = browser

    async def search_linkedin(self,keyword:str):
        url = f"https://www.linkedin.com/jobs/search/?keywords={keyword}"
        await self.browser.navigate(url)
        return await self.browser.take_screenshot("jobs.png")