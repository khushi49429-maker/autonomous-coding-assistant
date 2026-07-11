from llm import fix_bug

code = """
def divide(a, b):
    return a / b

print(divide(10, 0))
"""

print(fix_bug(code))