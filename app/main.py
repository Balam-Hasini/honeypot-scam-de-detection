from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Agentic HoneyPot API")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Agentic Honeypot Running"}
