import os
import json

def build_user():
    Joe = User(who_r_u())
    wd = os.getcwd()
    user_file = wd + "/user_profiles/" + Joe.name
    Joe.directory = user_file

    checkpoint_1 = checkin(Joe.directory)
    #True means new user, False means existing
    if checkpoint_1 == False:
        return existing_user(user_file)
    #Continues to build the user
    os.mkdir(user_file)
    diary_path = user_file+"/Diary_entries"
    os.mkdir(diary_path)
    print("Nice to meet you", Joe.name)
    Joe.age = Age()
    print("Thank you")
    export_user(Joe)
    return Joe

def who_r_u():
    name = input("What is your name?")
    # Boolean makes sure input is only characters A-Z
    if (any(char.isdigit() or char.isalpha() == False for char in name)) or len(name) == 0:
        print("Names cannot contain digits, spaces, or special characters. Let's try that again.")
        return who_r_u()

    return name

def Age():
    age = input("How old are you?")
    if (any(char.isdigit() == False for char in age)):
        print("Age is only expressed in numbers 0-9. Let's try that again.")
        return Age()

    return age


# Serves as one of two main functions
# Decker is the old Blade Runner

# Currently the REGEX is not working
# json.dumps() will create python object from json

def existing_user(user_file_path):
    user_file_path = f"{user_file_path}/About.json"
    '''Decker = open(user_file_path, "r")
    Decker = Decker.read()
    Decker_split = Decker.split("\n")
    name = Decker_split[0].split("=")
    name = name[1]
    Decker = User(name)
    Old = Decker_split[1].split("=")
    Decker.age = Old[1]
    print("Welcome back", Decker.name)
    return Decker'''

# We must ensure at least one backup when changing user files
def export_user(user):
    out_file_path = f"{user.directory}/About.json"
    out_file = open(out_file_path, 'w')
    serialized_user = {
            'name': user.name,
            'age': user.age,
            'directory': user.directory
    }
    json.dump(serialized_user, out_file)
    pass

def checkin(user_directory):
    if os.path.exists(user_directory):
        return False
    else:
        return True

class User:

    def __init__(self, name):
        self.name = name

    directory = ""
