from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from routes.upload import router as upload_router

# NEW IMPORTS
from database import engine
from models.song import Base

app = FastAPI(
    title="BeatSense AI",
    version="1.0.0"
)

# CREATE TABLES IF THEY DON'T EXIST
Base.metadata.create_all(bind=engine)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(upload_router)

@app.get("/")
def home():
    return {
        "message": "BeatSense AI Backend Running"
    }