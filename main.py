import asyncio
from agents import Runner
from my_agents.actor_agent import triage_agent


#to store the answer in the variable
#USING ASYNCH APPROACH

while True:
    input_task = input(f"Talk to Actor {triage_agent.name}:  ") #ask dynamic questions
    if input_task == "":
        break
    async def main():
            result = await Runner.run(triage_agent,input_task) 
            print(result.final_output)
        



    asyncio.run(main())