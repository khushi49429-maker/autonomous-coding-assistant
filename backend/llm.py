import os
import re
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


# Get API key
api_key = os.getenv("GEMINI_API_KEY")


# Gemini client
client = genai.Client(
    api_key=api_key
)



# =============================
# Gemini Model
# =============================

MODEL_NAME = "gemini-3.1-flash-lite"





# =============================
# Common Gemini Function
# =============================

def ask_gemini(prompt):

    try:

        response = client.models.generate_content(

            model=MODEL_NAME,

            contents=prompt

        )

        return response.text



    except Exception as e:


        error = str(e)


        if "429" in error or "RESOURCE_EXHAUSTED" in error:

            return """
⚠️ CodeMentor AI is temporarily unavailable.

Gemini API quota is reached.
Please wait and try again later.
"""


        return f"Error: {error}"







# =============================
# Test Connection
# =============================

def test_llm():

    return ask_gemini(
        "Say hello in one sentence."
    )







# =============================
# Generate Code
# =============================

def generate_code(prompt):

    prompt_text = GENERATE_PROMPT.format(
        prompt=prompt
    )

    return ask_gemini(
        prompt_text
    )







# =============================
# Explain Code
# =============================

def explain_code(code):

    prompt = EXPLAIN_PROMPT.format(
        code=code
    )

    return ask_gemini(
        prompt
    )







# =============================
# Review Code
# =============================

def review_code(code):

    prompt = REVIEW_PROMPT.format(
        code=code
    )

    return ask_gemini(
        prompt
    )







# =============================
# Fix Bug
# =============================

import re

# =============================
# Fix Bug
# =============================

def fix_bug(code):

    prompt = FIX_BUG_PROMPT.format(
        code=code
    )

    response = ask_gemini(prompt)

    # If Gemini didn't return a markdown code block,
    # wrap the corrected code automatically.
    if "```" not in response:

        match = re.search(
            r"Corrected Code:\s*(.*)",
            response,
            re.DOTALL
        )

        if match:

            fixed_code = match.group(1).strip()

            explanation = response[:match.start()].strip()

            response = (
                explanation
                + "\n\nCorrected Code:\n\n"
                + "```python\n"
                + fixed_code
                + "\n```"
            )

    return response