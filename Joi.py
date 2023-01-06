import Joi_funxtions
import Joi_statistics
import User_background
import jsonpickle

# We must collect data first

# It must score emotions from the sentiment

# It must ask questions

# It must interact with the user

### Load in the background of the use by checking in

Joe = User_background.build_user()

Diary = Joi_funxtions.Diary_entry(Joe)

Joi_funxtions.export_diary(Joe, Diary)

base = Joi_funxtions.baseline()

Joi_funxtions.export_baseline(Joe, base)

Joi_statistics.visualize_graph(Joe)