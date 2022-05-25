"""01_introduction_v2
this version is an improvement on 01_introduction_v1 """


# Functions
# This function will get the players name
def get_name():
    name = str(input("What is your name: "))
    return name


# This function will get the players age
def get_age():
    age = int(input("How old are you: "))
    if 1 <= age <= 100:
        return age

    else:
        print("<Error> please enter a valid whole number")
        return get_age()


# Main routine
name = get_name()
age = get_age()
print(f"Kia ora {name}. Welcome to The maori quiz.\n"
      f"Since you are {age} years old you will probably find this easy")

