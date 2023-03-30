import os
import jsonpickle as json

if __name__ == "__main__":
    print("Running in User_background.py")

def build_user():
    Joe = User(who_r_u())
    wd = os.getcwd()
    user_file = wd + "/user_profiles/" + Joe.name
    Joe.directory = user_file

    checkpoint_1 = checkin(Joe.directory)
    #True means new user, False means existing
    if checkpoint_1 == False:
        return existing_user(user_file)
    #Continues to build the user / Sends the populate to export function now
    print("Nice to meet you", Joe.name, "\n")
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

# json.dumps() will create python object from json

def existing_user(user_file_path):
    user_file_path = f"{user_file_path}/About.json"
    with open(user_file_path, 'r') as existing:
        rebuild = existing.read()
    # Decode takes the json format and transforms it back into an object with all the existing attributes
    Decker = json.decode(rebuild)
    print("\nWelcome back", Decker.name, "\n")
    return Decker

# We must ensure at least one backup when changing user files
def export_user(user):
    #Populate step
    os.mkdir(user.directory)
    diary_path = f"{user.directory}/Diaries"
    os.mkdir(diary_path)
    base_line_path = f"{user.directory}/Baselines"
    os.mkdir(base_line_path)
    out_file_path = f"{user.directory}/About.json"
    out_file = open(out_file_path, 'w')
    final = json.encode(user)
    out_file.write(final)
    pass

# Function to prevent overwriting an existing user object
def checkin(user_directory):
    if os.path.exists(user_directory):
        return False
    else:
        return True

class User:

    def __init__(self, name):
        self.name = name

    directory = ""


# This will change the interval in a user's About.json to allow for relection capabilities and the chance of it occuring
# Writted here because of jsonpickle and user handling
def change_interval(user, interval):
    # Stolen from resurrect function
    with open(user.directory+"/About.json", 'r') as raw:
        raw = raw.read()
        zombie = json.decode(raw)

    zombie.interval = interval
    #print(zombie)
    out_file_path = f"{user.directory}/About.json"
    out_file = open(out_file_path, 'w')
    final = json.encode(zombie)
    out_file.write(final)
    print("About.json updated!")