"""The first version of 03_questions"""


def questions():

    score = 0
    answer = input("are you ready to play?: ")
    if answer.lower() == "yes" or "y":
        answer = input("Question 1: What does Tahi mean in maori \n"
                           "a. 1 \n"
                           "b. 5 \n"
                           "c. 10 \n")

        while answer.lower() != "a":
            print("Wrong answer")
            break

        else:
            score += 1
            print("Correct")


# Main routine
questions()
print("next question continues")
