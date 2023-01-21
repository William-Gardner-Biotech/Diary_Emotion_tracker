import Joi_funxtions
import Joi_statistics
import User_background
import jsonpickle
import argparse
import os
import datetime

# We must collect data first

# Joi is designed to collect user diaries to help monitor a user's emotions.

parser = argparse.ArgumentParser(description='BladeRunner inspired Diary program. The longer you use this program the more accurate it will become.')

parser.add_argument('--date', required=False, type=str, default=None,
	metavar='<str>', help='Allows user to log missed days or import older diaries. [Must be in DDMonYYYY: ex 10Jun2021]')

parser.add_argument('--reflect', required=False, type=str, default=None,
	metavar='<str>', help='Allows user to add an emotional reflection after their baseline to explain what contributed to scores')

parser.add_argument('--interval', required=False, type=int, default=False,
	metavar='<int>', help='Enter desired number of days for reflection')

arg = parser.parse_args()

### Load in the background of the user by checking in or creating new profile

Joe = User_background.build_user()



# If new user initiated then it will generate but won't add their interval
if arg.interval:
	User_background.change_interval(Joe, arg.interval)
	exit()

# Checks if optional date was given then uses it as date or defaults to today
# CAUTION Nothing prevents date to be formatted correctly only checks for collision. This will break our plot if user enters incorrectly
# check that we aren't overriding existing data or an existing day with our backdate argument
# Relies on only checking Diary exists as the program treats both Diaries and Baselines together.

if arg.date:
	day = arg.date
	save_location = f'{Joe.directory}/Diaries/{day}.txt'
else:
	day = datetime.date.today()
	day = day.strftime("%d%b%Y")
	save_location = f'{Joe.directory}/Diaries/{day}.txt'

if os.path.exists(save_location):
	exit(f'COLLISION DETECTED!\nDiary and Baseline already exist for {day}. OVERRIDE PREVENTED')

Diary = Joi_funxtions.Diary_entry(Joe)

# This allows for reflection to be added
try:
	Diary+=Joi_funxtions.reflect(Joe, Diary)
except:
	pass

base = Joi_funxtions.baseline()

# Export together to prevent loss of data from interupts
if arg.date:
	Joi_funxtions.export_diary(Joe, Diary, arg.date)
	Joi_funxtions.export_baseline(Joe, base, arg.date)
else:
	Joi_funxtions.export_diary(Joe, Diary)
	Joi_funxtions.export_baseline(Joe, base)

Joi_statistics.visualize_graph(Joe)