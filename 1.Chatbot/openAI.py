from langchain_openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

try:
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("OPENAI_API_KEY not found in environment variables")
    
    llm = OpenAI(model="gpt-3.5-turbo", temperature=0.9)
    response = llm.invoke("What is the capital of France?")
    print(response)
except Exception as e:
    print(f"Error: {e}")

#result : api key not working 