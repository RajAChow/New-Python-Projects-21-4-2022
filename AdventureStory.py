while True:
    user_name = input("What is your name?: ")
    if user_name.isalpha() == True:
        print(f"Hi {user_name}\n")
        break
    else:
        print("Names can only have letters bruh")
        continue

def adventureTime():
    while True:
        choice1 = input("You wake up early in the morning, do you want to get up? (y/n): ")
        if choice1.lower() == "y":
            print("You get up, brush your teeth, eat breakfast and go to work")
            choice2()
        elif choice1.lower() == "n":
            print("You sleep in and realize a couple hours of later that you missed work")
            choiceA()
        else:
            print("Invalid answer")
        break

def choice2():
    while True:
        choice2 = input("\nWhile driving to work you pass out at the wheel, can you wake up in time? (y/n): ")
        if choice2.lower() == "y":
            print("You save yourself, but get pulled over by a cop")
            choice3()
        elif choice2.lower() == "n": 
            print("You crashed into oncoming traffic and die. The end. :(")
            break
        else:
            print("Invalid answer")
            continue
        break

def choice3():
    while True:
        choice3 = input("\nThe officer asks for license and registration, do you give it to him? (y/n): ")
        if choice3.lower() == "y":
            print("He does a background check and realizes your wanted for the murder of 67 people")
            choice4()
        elif choice3.lower() == "n":
            print("He asks you to step out of the vehicle")
            choice5()
        else:
            print("Invalid answer")
            continue
        break

def choice4():
    while True:
        choice4 = input("\nYou can either kill him now or drive away? (k/d): ")
        if choice4.lower() == "k":
            print("You kill the innocent officer and get away, but reconsider you life choices and turn yourself in. The")
            break
        elif choice4.lower() == "d":
            print("Before you're able to drive away, you find yourself surrounded, instead of giving up you fight and mange to kill\
                17 officers before you're put down yourself. The end.")
            break
        else:
            print("Invalid answer")
            
def choice5():
    while True:
        choice5 = input("\nDo you charge at him or surrender peacfully? (c/s): ")
        if choice5.lower() == "c":
            print("He shoots you dead, but not before you split him in half with your ghoul powers. The end.")
            break
        elif choice5.lower() == "s":
            print("He commends you for complying and you get sentenced to 48 life sentences. The end.")
            break
        else:
            print("Invalid answer")
    
def choiceA():
    while True:
        choiceA = input("\nYou get a call from your boss, do you pick up? (y/n): ")
        if choiceA.lower() == "y":
            print("He is screams at you and tells you that you're fired")
            choiceB()
        elif choiceA.lower() == "n": 
            print("You move on with your life like he never existed like a sigma. The end.")
            break
        else:
            print("Invalid answer")
            continue
        break

def choiceB():
    while True:
        choiceB = input("\nYou can either go plead with your boss or get revenge? (p/r): ")
        if choiceB.lower() == "p":
            print("You go to work to beg for your job back and he laughs in your face")
            choiceC()
        elif choiceB.lower() == "r": 
            print("You run into your workplace with a cold stick of butter in a tube sock")
            choiceD()
        else:
            print("Invalid answer")
            continue
        break

def choiceC():
    while True:
        choiceC = input("\nThis enrages you, do you attack him or cool down? (a/c): ")
        if choiceC.lower() == "a":
            print("You lunge at him, but he activates his sharingan")
            choiceE()
        elif choiceC.lower() == "n": 
            print("You calm down, he reveals it was a test and confirms thatyou failed\
                because you're a beta male. The end.")
            break
        else:
            print("Invalid answer")
            continue
        break

def choiceD():
    while True:
        choiceD = input("\nDo you only focus on getting revenge on your boss? (y/n): ")
        if choiceD.lower() == "y":
            print("You pummel his body mercilessly and live happily ever after. The end.")
            break
        elif choiceD.lower() == "n": 
            print("September 17th, 2074: The Butter Sock Workplace Incident. The end")
            break
        else:
            print("Invalid answer")
            continue

def choiceE():
    while True:
        choiceE = input("\nYou reveal that you have the rinnegan, do you spare him? (y/n): ")
        if choiceE.lower() == "y":
            print("He thanks you for sparing him, but back stabs you and awakens his mangekyou, you die. The end.")
            break
        elif choiceE.lower() == "n": 
            print("You annhilate him from existence, then go on to rule the world as the supreme all-powerful overlord")
            break
        else:
            print("Invalid answer")
            continue

adventureTime()