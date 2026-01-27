from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Você é um especialista em IA"},
        {"role": "user", "content": "Explique o que é LangChain em uma frase"}
    ]
)

print(response.choices[0].message.content)
