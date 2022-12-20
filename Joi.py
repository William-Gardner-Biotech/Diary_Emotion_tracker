import Joi_funxtions
import User_background

# We must collect data first

# It must score emotions from the sentiment

# It must ask questions

# It must interact with the user

### Load in the background of the use by checking in

Joe = User_background.build_user()

Day_score = Joi_funxtions.how_are_you()

Diary = Joi_funxtions.Diary_entry(Joe)

print(Diary)

