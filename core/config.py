from dotenv import load_dotenv
import  os

load_dotenv() #carrega as variaveis do .env onde coloquei as coisas do banco

DATABASE_URL = os.getenv("DATABASE_URL")
TOKEN_API = os.getenv("TOKEN_API")