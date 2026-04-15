import os

from dotenv import load_dotenv
load_dotenv()

API_URL = os.getenv("API_URL")
MODEL_NAME = os.getenv("MODEL_NAME")
TEMP = os.getenv("TEMP")

