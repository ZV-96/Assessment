"""01_introduction_v2
this version is an improvement on 01_introduction_v1 """


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


# Main routine
name = get_name()
age = get_age()
print(f"Kia ora {name}. Welcome to The maori quiz.\n"
      f"Since you are {age} years old you will probably find this easy")



