import warnings
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from src.schemas.chat_request import ChatRequest
from src.schemas.prompt import PromptRequest, PromptResponse
from src.services.Modulo2.aula_1.cohere_ai import generate_response
from src.services.Modulo2.aula_3.lang_graph_memoria_local import chat


warnings.filterwarnings(
    "ignore",
    message="Core Pydantic V1 functionality isn't compatible with Python 3.14 or greater.")

app = FastAPI(
    title="IA Playground API",
    description="API simples para gerar respostas de IA usando Cohere",
    version="1.0.0"
)

@app.get("/")
def health_check():
    return {"status": "ok", "message": "API rodando com sucesso"}

@app.post("/chat")
def chat_endpoint(payload: ChatRequest):
    return chat(
        message=payload.message,
        thread_id=payload.thread_id
    )

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
