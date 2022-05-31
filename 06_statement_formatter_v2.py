"""06_statement_formatter_v2
convert 06_statement_formatter_v1 into a function
lets user pick their own symbol and text
"""


# formats users text using there input text and symbol
def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# Main Routine
# ask user to input text and symbol to format and prints it
text1 = input("Enter the statement you want to format")
symbol1 = input("What symbol do you want to use")
print()
print(formatter(symbol1, text1))
