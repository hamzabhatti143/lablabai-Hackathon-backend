import asyncio
from agents import Runner
from my_agents.Coordinator_Agent import Coordinator_Agent

async def main():
    user_input = input("Enter Your Question: ")
    response = await Runner.run(starting_agent=Coordinator_Agent, input=user_input)
    print(response.final_output)

asyncio.run(main())