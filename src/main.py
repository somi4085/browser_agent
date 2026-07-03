import asyncio
from browser import BrowserController
from agents import VisionAgent
from actions import ActionExecutor
from memory import AgentMemory
from job_search import JobSearch 
from job_applier import JobApplier
from job_profile import JobProfile

asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

async def run_agent(task:str, url:str):
    browser = BrowserController()
    agent = VisionAgent()
    executor = ActionExecutor(browser)
    memory = AgentMemory()
    
    try:
        await browser.start()
        await browser.navigate(url)

        for i in range(5):
            screenshot = await browser.take_screenshot(f"step{i}.png")
            response = await agent.analyze_screenshots(screenshot, task+f"Previous steps: {memory.get_history()}")
            print(response)
            try:
                await executor.execute(response)
                memory.add_step(response, "success", True)
            except Exception as e:
                memory.add_step(response, str(e), False)
                memory.add_error(str(e))


    except Exception as e:
        print("Error:",e)
    finally:
        await browser.browser.close()

    
async def run_job_bot():
    browser = BrowserController()
    agent = VisionAgent()
    search = JobSearch(browser)
    applier = JobApplier(browser, agent)

    await browser.start()
    await search.search_linkedin(JobProfile.JOB_TITLE)
    await applier.apply_to_job("https://www.linkedin.com")



asyncio.run(run_agent(
    task="Search for machine learning on Google",
    url="https://www.google.com"))


asyncio.run(run_job_bot())

