import os
from google import genai
from dotenv import load_dotenv

from prompts import (
    EXPLAIN_PROMPT,
    GENERATE_PROMPT,
    REVIEW_PROMPT,
    FIX_BUG_PROMPT
)

# Load environment variables
load_dotenv()

# Read API key
api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=api_key)


# -----------------------------
# Test Gemini Connection
# -----------------------------
def test_llm():
    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents="Say hello in one sentence."
        )

        return response.text

    except Exception as e:
        return f"Error: {e}"


# -----------------------------
# Explain Code
# -----------------------------
def explain_code(code):
    try:
        prompt = EXPLAIN_PROMPT.format(code=code)

        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Error: {e}"


# -----------------------------
# Generate Code
# -----------------------------
def generate_code(prompt):
    try:
        text = GENERATE_PROMPT.format(prompt=prompt)

        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=text
        )

        return response.text

    except Exception as e:
        return f"Error: {e}"


# -----------------------------
# Review Code
# -----------------------------
def review_code(code):
    try:
        prompt = REVIEW_PROMPT.format(code=code)

        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Error: {e}"


# -----------------------------
# Fix Bugs
# -----------------------------
def fix_bug(code):
    try:
        prompt = FIX_BUG_PROMPT.format(code=code)

        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Error: {e}"