import Joi_funxtions
import Joi_statistics
import User_background
import jsonpickle
import argparse
import os
import datetime

# We must collect data first

# Joi is designed to collect user diaries to help monitor a user's emotions.

parser = argparse.ArgumentParser(
	description='BladeRunner inspired Diary program. The longer you use this program the more accurate it will become.',
	formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument('-d', '--date', required=False, type=str, default=None,
	metavar='<str>',
	help='Allows user to log missed days or import older diaries.\
		\nNOTE: Must be in DDMonYYYY format\
		\nEX: python Joi.py -d 10Jun2021 |OR| python Joi.py --date 10Jun2021')

parser.add_argument('-r', '--reflect', required=False, action='store_true',
	help='Allows user to add an emotional reflection after their baseline to explain what contributed to scores\
		\nNOTE: to use just include "-r" or "--reflect" in your command\
		\nEX: python Joi.py -r |OR| python Joi.py --reflect')

parser.add_argument('-i', '--interval' ,required=False, type=int, default=False, 
	metavar='<int>', 
	help='Enter desired number of days for reflection\
		\nNOTE: This will overwrite the previously stored reflection interval value, DEFAULT = 7\
		\nEX: python Joi.py -i 15 |OR| python Joi.py --interval 15')

parser.add_argument('-t', '--time_span', required=False, type=int, default=False,
	metavar='<int>', 
	help='Add a custom time span for visualizing your emotion graph.\
		\nNOTE: Primary purpose of this is to allow for more specified viewing of your recent diaries\
		\nEX: python Joi.py -t 7 |OR| python Joi.py --time_span 7')

parser.add_argument('-g', '--graph', required=False, type=int, default=False,
	metavar='<int>', 
	help='Used to view the emotion graph for a specific user, Provide the time span desired for the graph (time span must exceed 4) and user must have enough Diaries to view \
		\nNOTE: This command will only run the graph and will exit the program before recording Diary & Baseline\
		\nEX: python Joi.py -g 20 |OR| python Joi.py --graph 20')

arg = parser.parse_args()

# arg.graph must go before to avoid double-prompting

if arg.graph:
	temp_Joe = User_background.build_user()
	# cheap workaround that makes temp fake user and changes their time_span
	temp_Joe.time_span = arg.graph
	Joi_statistics.visualize_graph(temp_Joe)
	exit()

### Load in the background of the user by checking in or creating new profile

Joe = User_background.build_user()

# If new user initiated then it will generate but won't add their interval
if arg.interval:
	User_background.change_interval(Joe, arg.interval)
	exit()

if arg.time_span:
	User_background.change_time_span(Joe, arg.time_span)
	exit()

# Checks if optional date was given then uses it as date or defaults to today
# CAUTION Nothing prevents date to be formatted correctly only checks for collision. This will break our plot if user enters incorrectly
# check that we aren't overriding existing data or an existing day with our backdate argument
# Relies on only checking Diary exists as the program treats both Diaries and Baselines together.

if arg.date:
	if Joi_funxtions.validate_date(arg.date):
		day = arg.date
		save_location = os.path.join(Joe.directory, 'Diaries', f'{day}.txt')
	 	#save_location = f'{Joe.directory}/Diaries/{day}.txt'
	else:
		exit('Invalid Date input, Must be DDMonYYYY format,\ntry Joi.py -h for more help')
else:
	day = datetime.date.today()
	day = day.strftime("%d%b%Y")
	save_location = os.path.join(Joe.directory, 'Diaries', f'{day}.txt')
	#save_location = f'{Joe.directory}/Diaries/{day}.txt'


if os.path.exists(save_location):
	exit(f'COLLISION DETECTED!\nDiary and Baseline already exist for {day}. OVERRIDE PREVENTED')

# Executes Diary entry prompting

Diary = Joi_funxtions.Diary_entry(Joe)

# This allows for reflection to be added
# We are concatenating the Diary with our reflection to export using one step 
# Nice work around to temporarily change user interval to force a reflection
if arg.reflect:
	Joe.interval = 1
	Joi_funxtions.reflect(Joe, Diary)
else:
	try:
		Diary+=Joi_funxtions.reflect(Joe, Diary)
	except:
		pass

# Executes Baseline

base = Joi_funxtions.baseline()

# Export together to prevent loss of data from interupts
if arg.date:
	Joi_funxtions.export_diary(Joe, Diary, arg.date)
	Joi_funxtions.export_baseline(Joe, base, arg.date)
else:
	Joi_funxtions.export_diary(Joe, Diary)
	Joi_funxtions.export_baseline(Joe, base)

Joi_statistics.visualize_graph(Joe)