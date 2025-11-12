from decouple import config
from openai import AsyncOpenAI
from agents import OpenAIChatCompletionsModel

my_key = config("GEMINI_API_KEY")

base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"

my_client = AsyncOpenAI(api_key=my_key, base_url=base_url)

MODEL = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash" , openai_client=my_client
)