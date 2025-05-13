from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.routes.auth import router as auth_router

app = FastAPI(
    title="DevCore Auth Service",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def health_check():
    return {"status": "OK", "message": "Auth Service is running!"}
