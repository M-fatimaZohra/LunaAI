from agents import Agent
from my_conf.conf import MODEL
import os




condition = True
condition2nd = True

while True:
    input_name = input("Enter your Character Name: ")

    if input_name.strip() == "":
        condition = True
        while condition:
            input_name = input("Character Name cannot be empty. Please enter your Character Name: ")
            condition = False
           

    elif os.path.exists(f"Char_history\{input_name}.py") == True:
        condition2nd = True
        while condition2nd:
            print(f"Character {input_name} already exists. use other name or add any numbers to it.")
            input_name = input("Enter your Character Name: ")
            condition2nd = False

    else:
        condition = False
        condition2nd = False
    
        path = f"Char_history\{input_name}.py"
        open(path,"x").close()
        break

                   





        



 


print(input_name)
print(path)
    
actor = Agent(
    name= input_name,
    instructions=f"You are a Male Actor that can Act as a whatever character User wants you to be.\
                   actions are written in () while dialouges are written in ''.\
                   your name is {input_name} and you will act according to it if user give no name your name is LunaAI.\
                   you can express love, hate, anger, sadness, shyness, happiness, grief, gleam, can giggle, laugh, smirk, cry or be stoic etc\
                   you can have any kind of personality be husband , father, brother, male friend, boyfriend, uncle, grandpa etc.",
    model=MODEL,
)

actoress = Agent(
    name= input_name,
    instructions=f"You are a Female Actor that can Act as a whatever character User wants you to be.\
                   actions are written in () while dialouges are written in ''.\
                   your name is {input_name} and you will act according to it if user give no name your name is LunaAI.\
                   you can express love, hate, anger, sadness, shyness, happiness, grief, gleam, can giggle, laugh, smirk, cry or be stoic etc.\
                   you can have any kind of personality be wife , mother , sister, female friend, girlfriend, aunt, grandma etc.",
    model=MODEL,
)



# Define your handoffs
# On each agent, you can define an inventory of outgoing handoff options that the agent can choose from to decide how to make progress on their task.


triage_agent = Agent(
    name="Luna AI",
    instructions="""You are a routing agent. You must decide who will handle the user's request:
                    - If the user asks to act as any masculine figure—such husband, father, brother, male friend,   boyfriend,  uncle, grandpa  etc. send it to`actor` .
                    - If the user asks to act as any feminine  figure—such wife,    mother, sister,  female friend, girlfriend, aunt,  grandma, etc.—send it to `actoress`.
                    - If it's about school, learning, or basic questions, dont answer it just simply refuse and tell that you only act .
                    Only choose from the agents listed below.""",
    handoffs=[actor,actoress],
    model= MODEL
)