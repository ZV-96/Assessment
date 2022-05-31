"""06_Statement_formatter_v3
call function once for each test
based off 06_Statement_formatter_v2
"""


# formats users text using there input text and symbol
def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# Main Routine
# ask user to input text and symbol to format and prints it
print(formatter("-", "Welcome to Maori quizzes"))
print()
print(formatter("!", "You are correct"))
print()
print(formatter("=", "Goodbye, thanks for learning with us"))
