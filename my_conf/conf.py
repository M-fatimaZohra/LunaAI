from decouple import config
from openai import AsyncOpenAI
from agents import OpenAIChatCompletionsModel
from dotenv import load_dotenv
import os

load_dotenv(override=True)
my_key = os.getenv("GEMINI_API_KEY")

# my_key = config("GEMINI_API_KEY")
client = AsyncOpenAI(api_key=my_key,base_url="https://generativelanguage.googleapis.com/v1beta/openai/")
MODEL = OpenAIChatCompletionsModel(model="gemini-2.0-flash",openai_client=client)




