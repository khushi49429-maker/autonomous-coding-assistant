import os
from google import genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Read API key
api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=api_key)


# -----------------------------
# Test Function
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
        prompt = f"""
You are an expert software engineer.

Explain the following code in simple language.

Mention:
1. What the code does.
2. How it works.
3. Time Complexity.
4. Space Complexity.

Code:
{code}
"""

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
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=f"""
You are an expert software engineer.

Generate clean, efficient, and well-formatted Python code.

User Request:
{prompt}

Only return the code.
"""
        )

        return response.text

    except Exception as e:
        return f"Error: {e}"

# -----------------------------
# Review Code
# -----------------------------
def review_code(code):
    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=f"""
You are an expert software engineer and code reviewer.

Review the following code.

1. Overall summary
2. Bugs or logical errors
3. Code quality
4. Readability
5. Performance improvements
6. Best practices
7. Security issues
8. Rating out of 10

Code:
{code}
"""
        )

        return response.text

    except Exception as e:
        return f"Error: {e}"
 # -----------------------------
# fix_bug
# -----------------------------


def fix_bug(code):
    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=f"""
You are an expert software engineer and debugging specialist.

The following code may contain bugs.

Your tasks are:
1. Identify all bugs or errors.
2. Explain why each bug occurs.
3. Provide the corrected code.
4. Explain what changes you made.
5. Return the complete corrected code.

Code:
{code}

Return the answer in the following format:

## Bugs Found
...

## Explanation
...

## Corrected Code
...

## Changes Made
...
"""
        )

        return response.text

    except Exception as e:
        return f"Error: {e}"
        from prompts import (
    EXPLAIN_PROMPT,
    GENERATE_PROMPT,
    REVIEW_PROMPT,
    FIX_BUG_PROMPT,
    prompt_text = EXPLAIN_PROMPT.format(code=code)
)