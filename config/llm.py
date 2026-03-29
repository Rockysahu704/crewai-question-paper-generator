from crewai import LLM
import os
from dotenv import load_dotenv

load_dotenv()

llm = LLM(
    model="groq/llama-3.3-70b-versatile",   # ✅ MUST start with groq/
    api_key=os.getenv("GROQ_API_KEY"),  # ✅ correct param name
    temperature=0.7
)