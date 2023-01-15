import matplotlib.pyplot as plt
import os
import jsonpickle
import re
import datetime

# Fix error of dates being sorted but respective emotional scores don't associate
def visualize_graph(user):
    open_order = []
    Fear_y_axis = []
    Anger_y_axis = []
    Sad_y_axis = []
    Happy_y_axis = []
    baselines_path = user.directory+"/Baselines/"
    # This will list all files in the Baselines directory, must select file
    for root, dirs, file in os.walk(baselines_path):
        for i in file:
            date = (re.search("(\d){2}(...)(\d){4}", i)).group()
            open_order.append(date)

    # open_order is the same as x_axis_dates
    open_order.sort(key=lambda date: datetime.datetime.strptime(date, '%d%b%Y'))

    for date in open_order:
        filename = f"{baselines_path}BL_{date}.json"
        emotions = resurrect(filename)
        Fear_y_axis.append(float(emotions.Fear))
        Anger_y_axis.append(float(emotions.Anger))
        Sad_y_axis.append(float(emotions.Sad))
        Happy_y_axis.append(float(emotions.Happy))

    if len(open_order) < 5:
        return print("Plot could not be generated. \nI need more entries to generate a meaningful plot.")

    plt.plot(open_order, Fear_y_axis, label="FEAR")
    plt.plot(open_order, Anger_y_axis, label="ANGER")
    plt.plot(open_order, Sad_y_axis, label="SAD")
    plt.plot(open_order, Happy_y_axis, label="HAPPY")
    plt.legend()
    plt.show()
    return

def resurrect(BL_path):
    with open(BL_path, 'r') as raw:
        raw = raw.read()
        zombie = jsonpickle.decode(raw)
    return zombie

