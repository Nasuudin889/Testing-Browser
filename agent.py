import asyncio
import os
from dotenv import load_dotenv
from browser_use import Agent, BrowserSession
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()

# Get browser executable path from .env
browser_path = os.getenv("BROWSER_EXECUTABLE_PATH", r"C:\Program Files\Google\Chrome\Application\chrome.exe")

async def main():
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

    task = """
    1. Visit https://chromewebstore.google.com/detail/metamask/nkbihfbeogaeaoehlefnkodbefgpgknn
    2. Click "Add to Chrome" to install MetaMask extension
    3. After installation, go to chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html
    4. Follow steps to create a new wallet
    """

    browser_session = BrowserSession(
        executable_path=browser_path,
        headless=False
    )

    agent = Agent(
        task=task,
        llm=llm,
        browser_session=browser_session
    )

    result = await agent.run()
    print("✅ Task Completed:\n", result)

if __name__ == "__main__":
    asyncio.run(main())
