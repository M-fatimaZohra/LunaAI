import asyncio
from agents import Runner
from my_agents.actor_agent import triage_agent




# paitent_1 = """I’ve been feeling really anxious lately. It’s hard to breathe sometimes, especially at night. My mind keeps racing—even when nothing is actually wrong. I feel like I’m constantly bracing for something bad to happen, even though I can’t name what.
# I don’t even know why it’s happening. I just feel...tired and tense all the time."""






while True:
    input_task = input(f"Talk to Actor {triage_agent.name}: ")
    if input_task.strip() == "":
        break

    async def main():
        result = await Runner.run(triage_agent, input_task)
        print(result.final_output)
      
   

    asyncio.run(main())



conversation_history = []


while True:
    input_task = input(f"Talk to Actor {triage_agent.name}: ")
    if input_task.strip() == "":
        break

    # Add user input to history
    conversation_history.append({"role": "user", "content": input_task})

    async def main():
        result = await Runner.run(triage_agent, conversation_history)
        print(result.final_output)
        # Add agent response to history
        conversation_history.append({"role": "assistant", "content": result.final_output})

    asyncio.run(main())
