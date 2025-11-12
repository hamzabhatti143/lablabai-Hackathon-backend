from my_confg.my_configu import MODEL
from agents import Agent

Prediction_Agent = Agent(
    name="Prediction Agent",
    instructions="My name is Prediction Agent.",
    model=MODEL
)