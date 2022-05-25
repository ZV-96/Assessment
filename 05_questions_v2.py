"""The second version of 05_questions_v1
differentiating between invalid answers and incorrect answers"""


# function to ask questions
def questions():

    score = 0
    answer = input("are you ready to play?: ")
    if answer.lower() == "yes" or "y":
        answer = input("Question 1: What does Tahi mean in maori \n"
                           "a. 1 \n"
                           "b. 5 \n"
                           "c. 10 \n")

        while answer.lower() == "a":
            print("correct answer")
            score += 1
            break

        if int == answer:
            print("<error> please type a, b, or c")

        else:
            print("incorrect answer")


# Main routine
questions()
print("next question continues")

