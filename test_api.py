import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

model = GoogleGenerativeAI(api_key=api_key, model="gemini-2.5-flash")

print(model.invoke("Hello, how are you?"))