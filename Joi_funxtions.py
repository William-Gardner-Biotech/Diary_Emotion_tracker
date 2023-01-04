import random
import os
import datetime
import jsonpickle


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
    entry = ""
    print(
        'Please tell me about your day, Write as much as you would like. Press ENTER when you want to end a paragraph. PRESS ENTER again to finish entry\n')
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
        print("Please Continue\n")
        return False
    else:
        print("Input not recognized")
        return Diary_continue()

def export_diary(user, entry):
    day = datetime.date.today()
    day = day.strftime("%d%b%Y")
    export_path = user.directory+"/Diaries/"+day+".txt"
    # make this a forkable position to add an overwrite option (make overwrite a function)
    if os.path.exists(export_path):
        return ("Diary Entry already submitted for this date")
    with open(export_path, 'w') as submit:
        submit.write(entry)
    return print("Entry recorded")



if __name__ == '__main__':
    print("Running in function library")

# F A S H = {[Fear],[Anger],[Sad],[Happy]}

# baseline returns a pickled json object in the above format
def baseline(emotions=None):

    def Fear_fxn(emotions = None):
        Fear = input("Rate your level of Fear on a scale of 0-10: ")
        check1 = between1_10(Fear)
        if check1 != True:
            print("Answer must be within scale [No spaces or letters]\n")
            return baseline()
        else:
            emotions = basic_emotion(Fear)
            return mixer(emotions)

    def Anger_fxn(emotions = None):
        Anger = input("Rate your level of Anger on a scale of 0-10: ")
        check2 = between1_10(Anger)
        if check2 != True:
            print("Answer must be within scale [No spaces or letters]\n")
            return mixer(emotions)
        else:
            emotions.Anger = Anger
            return mixer(emotions)

    def Sad_fxn(emotions = None):
        Sad = input("Rate your level of Sadness on a scale of 0-10: ")
        check3 = between1_10(Sad)
        if check3 != True:
            print("Answer must be within scale [No spaces or letters]\n")
            return mixer(emotions)
        else:
            emotions.Sad = Sad
            return mixer(emotions)

    def Happy_fxn(emotions = None):
        Happy = input("Rate your level of Happiness on a scale of 0-10: ")
        check4 = between1_10(Happy)
        if check4 != True:
            print("Answer must be within scale [No spaces or letters]\n")
            return mixer(emotions)
        else:
            emotions.Happy = Happy
            return mixer(emotions)

# It is returning out but continues instead of returning

    def mixer(emotions=None):
        if emotions is None:
            return Fear_fxn(emotions)
        elif len(emotions.__dict__) == 1:
            return Anger_fxn(emotions)
        elif len(emotions.__dict__) == 2:
            return Sad_fxn(emotions)
        elif len(emotions.__dict__) == 3:
            return Happy_fxn(emotions)
        elif len(emotions.__dict__) == 4:
            print("Baseline Complete")
            return emotions

    raw_baseline = mixer()
    baseline_obj = jsonpickle.encode(raw_baseline)
    return baseline_obj

def between1_10(response):
    if response.isdigit() != True:
        return False
    if len(response) != 1 or len(response) == 0:
        if response != "10":
            return False
    return True

class basic_emotion:
    def __init__(self, Fear):
        self.Fear = Fear

### Export Section ###

def export_diary(user, entry):
    day = datetime.date.today()
    day = day.strftime("%d%b%Y")
    export_path = user.directory+"/Diaries/"+day+".txt"
    # make this a forkable position to add an overwrite option (make overwrite a function)
    if os.path.exists(export_path):
        return ("Diary Entry already submitted for this date")
    with open(export_path, 'w') as submit:
        submit.write(entry)
    return print("Entry recorded")

# null function example
def export_baseline(user, base):
    day = datetime.date.today()
    day = day.strftime("%d%b%Y")
    export_path = user.directory+"/Baselines/BL_"+day+".json"
    if os.path.exists(export_path):
        return ("Baseline already exists for this date")
    with open(export_path, 'w') as submit:
        submit.write(base)
