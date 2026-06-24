from dotenv import load_dotenv

import os

load_dotenv()

BASE_URL = os.getenv("BASE_URL")

REQUEST_TIMEOUT = int(
    os.getenv("REQUEST_TIMEOUT",10)
)