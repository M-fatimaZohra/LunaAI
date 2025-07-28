import os
import time

class LunaAI:
    def __init__(self):
        self.breaker = True
        self.breaker2nd = True
        self.condition = True
        self.condition2nd = True
        self.condition3rd = True
        self.gender =""
        self.input_name = ""
        self.path = ""
        self.read_file  = ""
        
    # complete the create_character method
    def create_character(self):

        #nameing
        while self.breaker:
            self.input_name = input("Enter your Character Name: ")
            self.path = f"Char_history\{self.input_name}.json"

            if self.input_name.strip() == "":
                self.condition = True
                while self.condition:
                    self.input_name = input("Character Name cannot be empty. Please enter your Character Name: ")
                    self.condition = False
                

            elif os.path.exists(self.path) == True:
                self.condition2nd = True
                while self.condition2nd:
                    print(f"Character {self.input_name} already exists. use other name or add any numbers to it.")
                    self.input_name = input("Enter your Character Name: ")
                    self.condition2nd = False

            else:
                self.condition = False
                self.condition2nd = False
            
                
                open(self.path,"x").close()
                

                #gender giving
                while self.breaker2nd:
                    input_gender = input(f"Enter Gender of {self.input_name}\n 0) Male\n 1) Female\n Enter your choice: ")

                    if input_gender.strip() == "":
                        self.condition3rd = True
                        while self.condition3rd:
                            input_gender = input("Character Gender cannot be empty. Please enter your Character Gender: ")
                            self.condition3rd = False
                        
                    elif input_gender not in ["0", "1"]:
                        self.condition3rd = True
                        while self.condition3rd:
                            print("Invalid choice. Please enter 0 for male or 1 for female")
                            self.condition3rd = False


                    elif input_gender == "0":
                        self.condition3rd = False
                        self.gender = "Male"
                        self.breaker2nd = False
                        self.breaker = False
                        break

                    elif input_gender == "1":
                        self.condition3rd = False
                        self.gender = "Female"
                        self.breaker2nd = False
                        self.breaker = False
                        break
                        

                    else:
                        self.condition3rd = True
                        while self.condition3rd:
                            print("Invalid choice. Please enter 0 for male or 1 for female ....")
                            self.condition3rd = False

                    
    # complete the load_character method
    def load_character(self):
        n = 0
        print("Available Characters:")
        characters = [f[:-5] for f in os.listdir("Char_history") if f.endswith(".json")]
        for char in characters:
            print(f"{n+1}) {char}")
            n += 1

        time.sleep(0.5)

        character = input("Type name of Character:  ")
        condition = True
        if character.strip() == "":
                condition = True
                while condition:
                    character = input("\nCharacter Name cannot be empty. Please enter your Character Name: ")
                    condition = False
            

        else:
            for c in characters:
                if character.lower() == c.lower():
                    print(f"Loading {c}...\n")
                    time.sleep(0.5)
                    self.input_name = c
                    self.path = f"Char_history\{self.input_name}.json"

                    
                    time.sleep(0.5)
                    print(f"{c} has been loaded.\n")
                    return
                
                elif character.lower() not in c.lower():
                    print(f"finding {character}...\n")
                    time.sleep(0.2)
                    continue
                
            print(f"No character found with the name {character}. Please try again.\n\n")
    

    #complete the delete_character method
    def delete_character(self):
        n = 0
        print("Available Characters:")
        time.sleep(0.5)
        print("which one you want to delete?:")

        characters = [f[:-5] for f in os.listdir("Char_history") if f.endswith(".json")]
       


        for char in characters:
            print(f"{n+1}) {char}")
            n += 1

        time.sleep(0.5)

        character = input("Type name of Character: ")
        
        condition = True
        if character.strip() == "":
                condition = True
                while condition:
                    character = input("\nCharacter Name cannot be empty. Please enter your Character Name: ")
                    condition = False
            

        else:
            for c in characters:
                if character.lower() == c.lower():
                    print(f"Deleting {c}...\n")
                    time.sleep(0.5)
                    os.remove(f"Char_history/{c}.json")
                    time.sleep(0.5)
                    print(f"{c} has been deleted.\n")
                    return
                
                elif character.lower() not in c.lower():
                    print(f"finding {character}...\n")
                    time.sleep(0.2)
                    continue
                
            print(f"No character found with the name {character}. Please try again.\n\n")

       
        



                
            
    def start_app(self):
         
         print("\nWelcome to LunaAI Character Creation")
         time.sleep(0.5)
         print("where you like to start from?")
         time.sleep(0.5)
         print("1) Create a new Character and start chat")
         time.sleep(0.5)
         print("2) Load an existing Character and start chat")
         time.sleep(0.5)
         print("3)Delete an existing Character")
         time.sleep(0.5)
         print("4) Exit")
         time.sleep(0.5)


         input_choice = input("\nEnter your choice: ")



         match input_choice:
             
             case "1":
                 self.create_character()
                 return "created"  #flags
                
             case "2":
                 self.load_character()
                 return "loaded" #flags
             case "3":
                 self.delete_character()
                 return "deleted" #flags
             case "4":
                 print("\nExiting LunaAI Character Creation")

                 exit()
             case _:
                 print("\nInvalid choice. Please try again.")
                 self.start_app()



luna_AI = LunaAI()
