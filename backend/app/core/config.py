# backend/app/core/config.py

import os
from pathlib import Path
from dotenv import load_dotenv

# 1) Try to load a .env file if one exists (you can add one later)
env_path = Path(__file__).parent.parent.parent / ".env"
load_dotenv(env_path)

# 2) Simply read from the environment, defaulting to empty strings
DATABASE_URL   = os.getenv("DATABASE_URL",   "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# 3) You can import these directly elsewhere:
#    from app.core.config import DATABASE_URL, OPENAI_API_KEY