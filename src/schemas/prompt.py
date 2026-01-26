# src/schemas/prompt.py

from pydantic import BaseModel, Field

class PromptRequest(BaseModel):
    prompt: str = Field(..., example="Explique o que é IA de maneira sucinta.")
    max_tokens: int = Field(100, example=500)

class PromptResponse(BaseModel):
    response: str
