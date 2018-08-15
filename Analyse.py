import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import AutoMinorLocator

# Import csv, parsing the date and using it as an index
df = pd.read_csv('speeds_back.csv', parse_dates=['Date'],usecols=[0,2,3], index_col=0)

fig, ax = plt.subplots(figsize=(20, 7))
df.plot(ax=ax)

# Formatting for the major step of the X axis
major_fmt_x = mdates.DateFormatter('%H:%M:')
hour_locator = mdates.HourLocator()
ax.xaxis.set_major_locator(hour_locator)
ax.xaxis.set_major_formatter(major_fmt_x)
plt.setp(ax.xaxis.get_majorticklabels(), rotation=90, fontsize=10, horizontalalignment='center')

# Formatting for the minor step of the X axis
min_locator = mdates.MinuteLocator(byminute=[15, 30, 45])
ax.xaxis.set_minor_locator(min_locator)
# minor_fmt_x = mdates.DateFormatter('%H:%M:')
# ax.xaxis.set_minor_formatter(minor_fmt_x)
# plt.setp(ax.xaxis.get_minorticklabels(), rotation=90, fontsize=8, horizontalalignment='center')

# Formatting for the minor step of the Y axis
minor_locator_y = AutoMinorLocator(2)
ax.yaxis.set_minor_locator(minor_locator_y)
plt.ylim([0, 8.5])

# plt.show()
plt.savefig('Internet Speeds.png')

