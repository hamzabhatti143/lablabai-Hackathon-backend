from my_confg.my_configu import MODEL
from agents import Agent

Greet_Agent = Agent(
    name="Greet Agent",
    instructions="""
You are a Greet Agent, and your name is Greet Agent.
Your job is to respond to the user’s greetings according to how the user greets you.
""",
model=MODEL
)
