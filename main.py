from fastapi import FastAPI
from pydantic import BaseModel
from rag_pipeline import RAGAssistant

app = FastAPI()
assistant = RAGAssistant()

class Query(BaseModel):
    question: str

@app.post("/chat")
def chat(query: Query):
    answer = assistant.answer(query.question)
    return {"response": answer}
