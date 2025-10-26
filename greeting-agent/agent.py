from google.adk.agents import Agent      #imports an agent

root_agent = Agent(                      #creation of an agent object
    name="greeting_agent",
    # https://ai.google.dev/gemini-api/docs/models
    model="gemini-2.0-flash",            #defines which model we are using
    description="Greeting agent",        #helps to understand the agent role
    instruction="""                      
    You are a helpful assistant that greets the user.             
    Ask for the user's name and greet them by name.
    """,
)
