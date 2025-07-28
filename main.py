import asyncio
from agents import Runner, set_tracing_disabled
from my_agents.actor_agent import triage_agent
import json
from my_agents.luna import luna_AI

set_tracing_disabled(True)


result = luna_AI.start_app()
if result == "deleted":
    
    print("===================================\n\n")
    


elif result== "created" or result == "loaded":
    

    # Plugging  starting to the agent
    if result in ["created", "loaded"]:
        conversation_history = []
        if result == "created":
            print(luna_AI.input_name)
            print(luna_AI.path)

        elif result == "loaded":
            with open(luna_AI.path, "r") as file:
                conversation_history = json.load(file)
            print(f"Loaded conversation history for {luna_AI.input_name} from {luna_AI.path}.\n")

            print(f"previous conversation history: {conversation_history}\n")




    while True:
        
        input_task = input(f"Talk to Actor {luna_AI.input_name}: ")
        if input_task.strip() == "":
            with open(luna_AI.path, "w") as file:
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
