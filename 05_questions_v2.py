"""The second version of 05_questions_v1
adding a list to make it random and able to loop"""


import random

# list of numbers for the questions
num_list = [[1, "tahi"], [2, "rua"], [3, "toru"], [4, "wha"], [5, "rima"], [6, "ono"], [7, "whitu"],
            [8, "waru"], [9, "iwa"], [10, "tekau"]]

# players score
player_score = 0
# Shuffle list
random.shuffle(num_list)
for i in num_list:
    # ask for user input
    attempt = input(f"What is the Maori word for {i[0]}?: ")
    if attempt == i[1]:
        # if users correct +1 to score then print correct
        player_score += 1
        print(f"Correct{player_score}")
    else:
        # if not print incorrect
        print("Incorrect")

# show player their final score
print(f"Your final score is {player_score}/10")
