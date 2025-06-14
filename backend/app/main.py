from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.api.health import router as health_router
from app.core.config import OPENAI_API_KEY
from .qa import answer_question

app = FastAPI(
    title="Medical Care Hub Backend",
    version="0.1.0"
)

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8100"],  # Your frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# mount health check (and later other routers) under /api
app.include_router(health_router, prefix="/api")

class QuestionRequest(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(req: QuestionRequest):
    answer = answer_question(req.question)
    return {"answer": answer}

@app.on_event("startup")
async def startup_event():
    # will print True once you add an OPENAI_API_KEY to .env
    print("OPENAI_API_KEY loaded:", bool(OPENAI_API_KEY))