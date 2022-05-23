"""The second version of 03_questions
differentiating between invalid answers and incorrect answers"""


def questions():

    error = "Invalid input"
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

        except ValueError:

        else:
            print("Incorrect answer")


# Main routine
questions()
print("next question continues")

