EXPLAIN_PROMPT = """
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

GENERATE_PROMPT = """
You are an expert software engineer.

Generate code in the language requested by the user.

User Request:
{prompt}

Return only the code.
"""

REVIEW_PROMPT = """
You are an expert code reviewer.

Review the following code.

Mention:
1. Summary
2. Bugs
3. Readability
4. Performance
5. Best Practices
6. Rating

Code:
{code}
"""

FIX_BUG_PROMPT = """
You are an expert debugging engineer.

Find and fix bugs.

Explain the bugs and return the corrected code.

Code:
{code}
"""