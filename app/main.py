import openai
import os
from dotenv import load_dotenv
from openai_integration import chat_with_assistant

# load environment variables
load_dotenv()

# get the api key
api_key = os.getenv("OPENAI_API_KEY")

if __name__ == "__main__":
    chat_with_assistant()

