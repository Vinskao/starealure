from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(api_key=api_key)  # Use the API ke$ from the environment

# Capture the response from the invoke method
response = llm.invoke("你好嗎!")

# Print the response
print(response)