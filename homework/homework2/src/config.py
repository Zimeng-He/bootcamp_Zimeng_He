# src/config.py
from pathlib import Path
from dotenv import load_dotenv
import os

def load_env(env_file: str = ".env"):
    env_path = Path(__file__).resolve().parents[1] / env_file
    load_dotenv(dotenv_path=env_path)
    print(f".env loaded from {env_path} (if present)")

def get_key(key: str, default: str | None = None) -> str | None:
    return os.getenv(key, default)