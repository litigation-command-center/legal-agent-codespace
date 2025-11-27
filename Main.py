# openrouter_adapter - place at top of main.py
import os

# REQUIRED: set these as Codespaces repository secrets (see instructions below)
OPENROUTER_KEY = os.getenv("OPENROUTER_API_KEY") or os.getenv("OPENAI_API_KEY")
OPENROUTER_BASE = os.getenv("OPENROUTER_API_BASE", "https://openrouter.ai/api/v1")

if not OPENROUTER_KEY:
    raise RuntimeError("Missing OpenRouter API key. Set OPENROUTER_API_KEY as a secret in Codespaces.")

# For libraries that respect OPENAI_API_KEY / OPENAI_API_BASE env vars:
os.environ["OPENAI_API_KEY"] = OPENROUTER_KEY
os.environ["OPENAI_API_BASE"] = OPENROUTER_BASE

# If the code constructs an OpenAI client directly, here's a helper (optional):
try:
    from openai import OpenAI
    openai_client = OpenAI(api_key=OPENROUTER_KEY, base_url=OPENROUTER_BASE)
except Exception:
    # If the project uses a different OpenAI client, environment overrides will still work.
    openai_client = None

# Now continue importing the rest of your Unwind/Agno app modules
