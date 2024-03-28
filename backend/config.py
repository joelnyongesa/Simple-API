from dotenv import load_dotenv
import os

load_dotenv()

class ApplicationConfig():
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URI"]
    SECRET_KEY = os.environ["SECRET_KEY"]