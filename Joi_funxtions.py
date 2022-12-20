import os
import random

def how_are_you():
    prompt = "How are you? [Rate your day on a scale of 1 to 10]"
    response = input(prompt)
    if response.isdigit() != True:
        print("Non digit, Try Again")
        return how_are_you()
    if len(response) != 1:
        if response != "10":
            print("Outside of 1-10 bound, Try Again")
            return how_are_you()
    return judge_howRU(response)

    # can pass a string through
def judge_howRU(how_r_u):
    how_r_u = int(how_r_u)
    if how_r_u == 10:
        print("Excellent, that makes me so happy")
    # 7-9
    elif how_r_u > 6 and how_r_u < 10:
        print("Wow, now that's good to hear")
    # 3-6
    elif how_r_u > 2 and how_r_u < 7:
        print("Averge Days have to happen")
    else:
        print("It gets better, would you like a compliment?")

    return how_r_u

def Diary_entry(user):
    Diary_directory = user.directory+"/Diaries"
    entry = ""
    print(
        'Please tell me about your day, Write as much as you would like. Press ENTER when you want to end a paragraph. PRESS ENTER again to finish entry')
    while True:
        line = input()
        if line:
            entry += f"{line}"
        else:
            if Diary_continue() == False:
                continue
            else:
                return entry

def Diary_continue():
    decision = input("ENTER key detected, would you like to end your entry? [Y or N]")
    #
    if len(decision) != 1:
        print("Input not recognized")
        return Diary_continue()

    decision=decision.upper()
    print(decision)
    if decision == "Y":
        return True
    elif decision == "N":
        print("Please Continue")
        return False
    else:
        print("Input not recognized")
        return Diary_continue()