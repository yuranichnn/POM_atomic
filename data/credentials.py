import os

from dotenv import load_dotenv

load_dotenv()

class Credentials:
    ADMIN_LOGIN = os.getenv("USERNAME")
    ADMIN_PASSWORD = os.getenv("PASSWORD")
