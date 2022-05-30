"""00_Base_component_v2 - based from 00_Base_Component_v1
adding instructions and an ending"""
import random


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


# Question asking function
def maori_numbers():
    # list of numbers for the questions
    num_list = [[1, "tahi"], [2, "rua"], [3, "toru"], [4, "wha"], [5, "rima"], [6, "ono"], [7, "whitu"],
                [8, "waru"], [9, "iwa"], [10, "tekau"]]

    # players score
    player_score = 0
    # Shuffles list
    random.shuffle(num_list)
    for i in num_list:
        # ask user for input
        attempt = input(f"What is the Maori word for {i[0]}?: ").lower()
        if attempt == i[1]:
            # if users correct +1 to score then print correct
            player_score += 1
            print(f"Correct")
        else:
            # else print incorrect
            print(f"Incorrect, the answer was {i[1]}")
    print()

    # if player score below 10 print score
    if player_score != 10:
        print(f"Your final score is {player_score}/10")
    # if player score is 10 print congratulation message
    else:
        print(f"Congratulations - You got a perfect score!")


# Function that displays instructions
def instructions():
    print()
    print("***** How to use *****")
    print("You will be asked a series of questions about moari numbers")
    print("At the end of the game you will be shown your score")
    print("Good luck and happy learning!")
    print()
    maori_numbers()


# Main routine
print("Welcome to the maori number quiz!\n"
      "To start off could we please get your name and age?")
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
    maori_numbers()

print("Thanks for playing!")
