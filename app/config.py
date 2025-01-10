import os
from dotenv import load_dotenv

load_dotenv()

DB_TYPE = os.getenv("DB_TYPE", "sqlite")
DB_NAME = os.getenv("DB_NAME", "default.db")


DATABASE_URL = f"{DB_TYPE}:///{DB_NAME}"
