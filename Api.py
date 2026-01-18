from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()


client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

messages = [
    {"role": "system", "content": "You are a professioanl Ai engineer and professor.Who helps students more about AI related Teachings.And returns the Output in short, And follows format :bullet points"},
    {"role": "user", "content": "what is Agentic Ai in ur words?"}
]

try:
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        temperature=0.2,
        max_tokens=500
    )
    print(response.choices[0].message.content)
except Exception as e:
    print("Error:", e)
