import os
import cohere
from dotenv import load_dotenv

load_dotenv()

API_KEY=os.getenv("COHERE_KEY")


co = cohere.Client(api_key=API_KEY)


def generate_response(prompt: str, max_tokens: int = 100) -> str:
    """Gera resposta da IA a partir do prompt usando a API Chat atual."""
    response = co.chat(
        model="command-a-03-2025",          # ou "command", "command-r-plus"
        message=prompt,             # <-- NÃO é prompt=
        max_tokens=max_tokens
    )
    return response.text.strip()    # <-- NÃO existe generations[]



if __name__ == "__main__":
    resposta = generate_response("Explique o que é IA em 1 frase.", max_tokens=50)
    print(resposta)
