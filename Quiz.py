import random

questions = {
    "q1": "The Earth round?: ", 
    "q2": "The current year 2014?: ",
    "q3": "All computers are purple",
    "q4": "My favourite colour is red",
    "q5": "",
    "q6": "",
    "q7": "",
    "q8": "",
    "q9": "",
    "q10": "",
}

while True:
    play_quiz = input("Do you want to take the True or False quiz? Yes or no? ")
    play_quiz.lower()
    if play_quiz == "yes":
        continue
    elif play_quiz == "no":
        print("Ending quiz")
        break
    else:
        print("Invalid input")
        
def quiz():
    input(questions["q1"])

print()
