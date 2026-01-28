# src/main.py

from fastapi import FastAPI, HTTPException
from src.schemas.prompt import PromptRequest, PromptResponse
from src.services.Modulo2.aula_1.cohere_ai import generate_response
from src.utils.clear_warning import clear_warn

app = FastAPI(
    title="IA Playground API",
    description="API simples para gerar respostas de IA usando Cohere",
    version="1.0.0"
)

clear_warn()

@app.get("/")
def health_check():
    return {"status": "ok", "message": "API rodando com sucesso"}

@app.post("/generate", response_model=PromptResponse)
def generate_text(body: PromptRequest):
    try:
        result = generate_response(
            prompt=body.prompt,
            max_tokens=body.max_tokens
        )
        return {"response": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
