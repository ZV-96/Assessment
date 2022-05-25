"""00_Base_component_v1
components added after they have been created and tested"""


# Functions
# Integer checking function - loops until a valid number is entered
def integer_checker(question):

    error = "\nSorry, you must enter an whole number\n"
    number = ""
    while not number:

        try:
            number = int(input(question))
            return number

        except ValueError:
            print(error)


# This function will get the players name
def get_name():
    name = str(input("What is your name: "))
    return name


# This function will get the players age
def get_age():
    age = integer_checker("How old are you: ")
    return age


# Yes/No Checker Function
def yes_no(question_text):
    while True:

        # Ask the user if they have played before
        answer = input(question_text).lower()

        # if they say yes, output 'Program Continues'
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # If they say no, output 'display Instructions'
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        # Otherwise - show error
        else:
            print("Please answer 'yes' or 'no'")


# Function that displays instructions
def instructions():
    print("***** How to use *****")
    print()
    print("The rules of the quiz will go here")
    print()
    print("Program continues")
    print()


# Main routine
name = get_name()
age = get_age()
print()
print(f"Kia ora {name}. Welcome to The maori quiz.\n"
      f"Since you are {age} years old you will probably find this easy")
print()

played_before = yes_no("Have you used this quiz before? : ")

if played_before == "No":
    instructions()

else:
    print("Program continues")
