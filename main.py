import asyncio
from agents import Runner
from my_agents.actor_agent import triage_agent,input_name, path
import json

conversation_history = []

input_name 

while True:
    
    input_task = input(f"Talk to Actor {input_name}: ")
    if input_task.strip() == "":
        with open(path, "w") as file:
            json.dump(conversation_history,file)


        break

    # Add user input to history
    conversation_history.append({"role": "user", "content": input_task})

    async def main():
        result = await Runner.run(triage_agent, conversation_history)
        print(result.final_output)
        # Add agent response to history
        conversation_history.append({"role": "assistant", "content": result.final_output})

    asyncio.run(main())
