# 🤖 AI Browser Agent with Gemini & Metamask Automation

This project uses the [browser-use](https://github.com/browser-use/browser-use) framework with Google Gemini (via LangChain) to automate browser tasks such as installing MetaMask and creating a new wallet.

## ✨ Features

- Runs a browser with full AI agent control.
- Uses Google Gemini 1.5 Flash as the LLM.
- Can interact with MetaMask and other browser extensions.
- Easy to switch browsers (like Chromium, Brave, etc.).

## 📁 Project Structure

my-browser-agent/
│
├── agent.py # Main Python script
├── .env # Environment variables (keep secret)
├── requirements.txt # Required Python packages
├── .gitignore # Files to ignore in Git
└── README.md # This file

yaml
Copy
Edit

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2. Create and Activate Virtual Environment (Optional)
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/macOS
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Add Your API Key
Create a .env file with this content:

ini
Copy
Edit
GOOGLE_API_KEY=your_gemini_api_key_here
Get your API key from Google AI Studio.

🚀 Run the Agent
bash
Copy
Edit
python agent.py
The AI agent will open a browser, install MetaMask from the Chrome Web Store, and follow the onboarding steps.

🌐 Switching Browsers
You can change the browser by modifying the agent.py file:

python
Copy
Edit
browser_name = "chromium"  # Change to "chrome", "brave", etc.
Make sure the path is correctly set for your browser if it's not in the system path.

🛑 Disclaimer
This project is for educational and research purposes only. Be careful when using it with sensitive information like wallet accounts.

📃 License
MIT License

yaml
Copy
Edit

---

If you'd like, I can also push this directly into the ZIP or generate a GitHub repo template for you. Just let me know!







