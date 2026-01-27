import os
import cohere
from dotenv import load_dotenv

load_dotenv()

API_KEY=os.getenv("COHERE_API_KEY")


co = cohere.Client(api_key=API_KEY)


def generate_response(
    prompt: str, 
    max_tokens: int = 1000,
    model: str = "command-a-03-2025"
    ) -> str:
    
    """Gera resposta da IA a partir do prompt usando a API Chat atual."""
    response = co.chat(
        model=model,         
        message=prompt,            
        max_tokens=max_tokens
    )
    return response.text.strip()   



if __name__ == "__main__":
    resposta = generate_response(prompt="Plutão é um planeta? Responda de maneira concisa.")
    print(resposta)
