import os
from dotenv import load_dotenv

load_dotenv()

config = {
    "PORT": os.getenv("PORT"),
    "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY"),
    "GROK_API_KEY": os.getenv("GROK_API_KEY"),
}
