from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="DevCore Gateway Service")


@app.get("/")
def root():
    return {
        "message": "Gateway is running!",
        "user_service": os.getenv("USER_SERVICE_URL"),
        "book_service": os.getenv("BOOK_SERVICE_URL")
    }
