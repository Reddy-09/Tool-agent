🧠 Tool Agent Example
🚀 Overview

This project demonstrates how to build a Tool Agent using the Google Agent Development Kit (ADK).
A Tool Agent extends the basic ADK agent by integrating tools that allow it to perform tasks beyond text generation — such as searching the web, executing code, or running custom Python functions.

This implementation showcases how to configure and use both built-in tools (like Google Search) and custom function tools, giving agents enhanced capabilities to retrieve information and take action dynamically.

⚙️ What is a Tool Agent?

A Tool Agent is an intelligent agent capable of using external tools to accomplish tasks more efficiently.

For example, instead of simply replying with text, your agent can:

Search the web for the latest news

Execute Python code snippets

Query your own data using Vertex AI Search

🔑 Key Components
🧩 1. Built-in Tools

ADK provides several built-in tools ready to use:

Google Search → Search the web for real-time information

Code Execution → Run code snippets and get outputs instantly

Vertex AI Search → Search within your private datasets

⚠️ Note: Each agent can only use one built-in tool at a time. See the ADK documentation
 for more details.


 ⚙️ 2. Custom Function Tools

Custom function tools allow you to extend agent functionality using your own Python functions.

✅ Best Practices:

Parameters: Use standard JSON-serializable types (str, int, list, dict)

No Default Values: Avoid default parameters

Return Type: Prefer returning a dictionary

If not, ADK will wrap it as `{"result": ...}`

Best format →` {"status": "success", "error_message": None, "result": "..."}`

Docstrings: Write clear docstrings since they serve as the tool’s description for the LLM

⚠️ Limitations
🚫 Single Built-in Tool Restriction

Currently, each root or single agent supports only one built-in tool.

```python
root_agent = Agent(
    name="RootAgent",
    model="gemini-2.0-flash",
    description="Root Agent",
    tools=[built_in_code_execution, google_search],  # ❌ NOT SUPPORTED
)
```
🚫 Built-in vs. Custom Tools

You cannot mix built-in tools with custom tools in the same agent.

```python
def get_current_time() -> dict:
    """Get the current time in the format YYYY-MM-DD HH:MM:SS"""
    return {
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

root_agent = Agent(
    name="RootAgent",
    model="gemini-2.0-flash",
    description="Root Agent",
    tools=[google_search, get_current_time],  # ❌ NOT SUPPORTED
)
```
💻 Implementation Example
🧠 Understanding the Code

The ```agent.py``` file defines a tool agent that uses Google Search to find real-time web information.

Configured with:

Agent name and description

Gemini model (```gemini-2.0-flash```)

Clear instructions for behavior and tool usage

Access to the ```google_search``` tool

A commented-out example of ```get_current_time()``` is also included — you can uncomment it to explore custom function tool capabilities.



⚡ Getting Started
🔧 Setup Instructions

1.Activate the virtual environment:

```
bash
# macOS/Linux
source ../.venv/bin/activate

# Windows CMD
..\.venv\Scripts\activate.bat

# Windows PowerShell
..\.venv\Scripts\Activate.ps1
```
2.Set up your API Key:

Rename .env.example → .env inside the tool_agent folder

Add your Google API Key:
bash
```
GOOGLE_API_KEY=your_google_api_key_here
```
▶️ Running the Example

1.Navigate to the 2-tool-agent directory

2.Start the interactive web UI:

bash

```
adk web
```
3.Open the displayed URL (usually http://localhost:8000)

4.From the dropdown, select “tool_agent”

5.Start chatting in the text box at the bottom


ADK CLI Options

```adk web``` → Launches the web chat UI

```adk run tool_agent``` → Runs the agent in terminal mode

```adk api_server``` → Starts a FastAPI server for testing API calls


💬 Example Prompts

Try these prompts in your chat UI:

“Search for recent news about artificial intelligence”

“Find information about Google’s Agent Development Kit”

“What are the latest advancements in quantum computing?”

Stop the conversation anytime using Ctrl + C in the terminal.


📸 Sample UI Screenshot

<img width="707" height="737" alt="Trace" src="https://github.com/user-attachments/assets/54fed392-1885-43f5-b3f3-814b11bd51a2" />
<img width="667" height="167" alt="agent tool-event" src="https://github.com/user-attachments/assets/a85017a4-1f15-4f54-bd7d-6cc348f25692" />
<img width="1893" height="602" alt="agent tool-2" src="https://github.com/user-attachments/assets/7af3d12e-d9c6-49dd-a04a-ab29abf234b6" />
<img width="1893" height="706" alt="agent tool-1" src="https://github.com/user-attachments/assets/d4d11b1b-da02-4876-a65d-52d2c2a12c50" />


👨‍💻 Developer Information

Project Author: Kyadhari Sai Deepak Reddy

Domain: AI Agent Development & Data Analytics

Technology Stack: Python · ADK · Gemini 2.0 · Google API
