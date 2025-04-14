from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

def create_app():
    load_dotenv()
    app = Flask(__name__)
    CORS(app)
    
    from app.routes.upload import upload_bp
    from app.routes.ask import ask_bp
    from app.routes.summarize import summarize_bp
    
    app.register_blueprint(upload_bp)
    app.register_blueprint(ask_bp)
    app.register_blueprint(summarize_bp)
    
    return app