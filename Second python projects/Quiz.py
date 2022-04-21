from PIL import Image
import random
#This is a list containing the questions already asked by the quiz
asked = []

#This is a dictionary containing the questions for the quiz
questions = {
    1: "The Earth is round?: ", 
    2: "The current year is 2014?: ",
    3: "All computers are purple?: ",
    4: "There are 9 CDs in this picture?: ",
    5: "Computer science is awesome?: ",
    6: "There are 6 continents in the world?: ",
    7: "This test is hard?: ",
    8: "Is this the cover to Kanye's unreleased album Yandhi?: ",
    9: "There are 14 questions on this test?: ",
    10: "The order of this test is random?: ",
}

#This is a dictionary containing the answers for the quiz
answers = {
    1: "true", 
    2: "false",
    3: "false",
    4: "false",
    5: "true",
    6: "false",
    7: "true",
    8: "true",
    9: "false",
    10: "true",
}
     
#This function is what asks the user the quiz questions and keeps score   
def quiz():
    score = 0
    asked = []
    #This boolean assures that the test is finished
    while len(asked) != 10:
        #This chooses a random number for the key to ask a question, meaning the test is always randomly ordered
        random_question = random.randint(1,10)
        #This assures that a question is not repeated
        if random_question not in asked:
            #This adds an unused question to a used question list
            asked.append(random_question)
            while True:
                #if the random number chosen is one of the 2 key values below, a corresponding image will be displayed
                if random_question == 8:
                    yandhi_image = Image.open('yandhi.jpg')
                    yandhi_image.show()
                if random_question == 4:
                    computer_image = Image.open('computer.png')
                    computer_image.show()
                #This finally asks the user the chosen question
                user_answer = input(questions[random_question])
                check_answer = user_answer.isalpha()
                #This assures only letters are in the user's answer and tells the user if there are non=alpha characters
                if check_answer != True or (user_answer.lower() != "true" and user_answer.lower() != "false"):
                    print("Invalid asnwer")
                    continue
                else:
                    #This keeps the score of the test, calling a function to change the user's score
                    score += changeScore(random_question, user_answer.lower())
                    break
    final_score = (score / 10) * 100
    print(f"You scored {score} out of 10! That's a percentage of {final_score}%")

#This function compares key values at the question and answer list to see if the user got the right answer
def changeScore(question_number, answer):
    if answer == answers[question_number]:
        return 1
    else:
        return 0
 
 #This is the function that runs the quiz() function and asks if they want to play, replay or quit 
def takeQuiz():   
    times_taken = 0
    while True:
        if times_taken == 0:
            play_quiz = input("Do you want to take the True or False quiz? Yes or no? ")
            times_taken += 1
        else:
            play_quiz = input("Do you want to retake the True or False quiz? Yes or no? ")
        if play_quiz.lower() == "yes":
            quiz()
            continue
        elif play_quiz.lower() == "no":
            print("Ending quiz")
            break
        else:
            print("Invalid input")
            
takeQuiz()
