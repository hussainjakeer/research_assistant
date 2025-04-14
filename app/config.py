import os

class Config:
    UPLOAD_FOLDER = "uploads"
    VECTORSTORE_FOLDER = 'app/vectorstores'
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")