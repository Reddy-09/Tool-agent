from google.adk.agents import Agent
from google.adk.tools import google_search
import datetime # ADDED: Required for the time tool

def get_current_time() -> dict: # FIXED: No space before 'def'
#     """
#     Get the current time in the format YYYY-MM-DD HH:MM:SS
#     """
    # NOTE: You may need to use 'datetime.datetime.now()' if you only use 'import datetime'
    return {
        "current_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
     }

root_agent = Agent(
    name="tool_agent", # NOTE: Changed name to match folder name for consistency (was "tool-agent")
    model="gemini-2.0-flash",
    description="Tool agent",
    instruction="""
    You are a helpful assistant that can use the following tools:
    - google_search
    """,
    tools=[google_search],
    # To enable the custom tool, you would change the line above to:
    # tools=[google_search, get_current_time],
)