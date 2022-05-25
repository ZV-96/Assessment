"""Yes/no checking component - Based on 02_yes_no_check_v1
adding the ability to say y instead of yes"""

# Ask the user if they have played before
show_instructions = input("Have you played this game before?: ").lower()

# if they say yes, output 'Program Continues'
if show_instructions == "yes" or show_instructions == "y":
    print("program continues")

# If they say no, output 'display Instructions'
elif show_instructions == "no" or show_instructions == "n":
    print("Display instructions")

# Otherwise - show error
else:
    print("Please answer 'yes' or 'no'")

print(f"You entered '{show_instructions}'")
