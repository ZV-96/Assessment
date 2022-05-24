"""01_introduction_v2
this version is a improvement on 01_introduction_v1 """


def get_name():
    name = str(input("What is your name: "))
    return name


def get_age(): # This function will get the players age
    age = int(input("How old are you: "))
    return age


# Main routine
name = get_name()
age = get_age()
print(formatter("-", f"Kia ora {name}. Welcome to Mamae Roro.\n"
      f"Since you are {age} years old you will probably find this easy"))

