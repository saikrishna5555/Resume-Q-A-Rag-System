from fastapi import FastAPI
from pydantic import BaseModel
from main import generation


class AskQuestion(BaseModel):
    question:str

app=FastAPI(title="do you want to know my self")

@app.get("/")
def greet():
    return {
        "message":"hai its working"
    }
@app.post("/chat")
def chat(ask:AskQuestion):
    return {
        "question" : ask.question,
        "response" : generation(ask.question)
    }