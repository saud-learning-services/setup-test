from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv('CANVAS_API_TOKEN')
API_DOMAIN = os.getenv('CANVAS_API_DOMAIN')
