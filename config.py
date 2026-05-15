import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'chave-fallback'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///intellicore.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    