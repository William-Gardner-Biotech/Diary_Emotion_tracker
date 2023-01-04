import matplotlib.pyplot as plt
import os
import jsonpickle
import re
import datetime

# Fix error of dates being sorted but respective emotional scores don't associate
def visualize_graph(user):
    x_axis_dates = []
    Fear_y_axis = []
    Anger_y_axis = []
    Sad_y_axis = []
    Happy_y_axis = []
    baselines = user.directory+"/Baselines/"
    # This will list all files in the Baselines directory, must select file
    for root, dirs, file in os.walk(baselines):
        for i in file:
            emotions = resurrect(baselines+"/"+i)
            # RE that finds the date only in "%d%b%Y" format
            date = (re.search("(\d){2}(...)(\d){4}", i)).group()
            # print(date)
            x_axis_dates.append(date)
            Fear_y_axis.append(float(emotions.Fear))
            Anger_y_axis.append(float(emotions.Anger))
            Sad_y_axis.append(float(emotions.Sad))
            Happy_y_axis.append(float(emotions.Happy))
    if len(x_axis_dates) < 5:
        return print("Not Enough Entries to generate a meaningful plot.")
    x_axis_dates.sort(key=lambda date: datetime.datetime.strptime(date, '%d%b%Y'))
    #x_axis_dates = matplotlib.dates.datestr2num(x_axis_dates)
    plt.plot(x_axis_dates, Fear_y_axis, label = "FEAR")
    plt.plot(x_axis_dates, Anger_y_axis, label = "ANGER")
    plt.plot(x_axis_dates, Sad_y_axis, label="SAD")
    plt.plot(x_axis_dates, Happy_y_axis, label="HAPPY")
    plt.legend()
    plt.show()
    return

def resurrect(BL_path):
    with open(BL_path, 'r') as raw:
        raw = raw.read()
        zombie = jsonpickle.decode(raw)
    return zombie