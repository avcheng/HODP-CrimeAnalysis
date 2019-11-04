import pandas as pd
import matplotlib.pyplot as plt

# Imports and reads only "reported" time
df = pd.read_csv("clean_crimes.csv")
analysis = df['reported']

# Finds hour for each report
dateFormat = '%Y-%m-%d %H:%M:00+00:00'
analysis = pd.to_datetime(analysis, format=dateFormat).dt.hour
analysis = analysis.value_counts().reset_index().rename(columns={'index': 'Time',
                                                                 'reported': 'Count'})
analysis = analysis.sort_values(by='Time')
analysis['Time'] = analysis['Time'].map({0: "12 AM",
                                         1: "1 AM",
                                         2: "2 AM",
                                         3: "3 AM",
                                         4: "4 AM",
                                         5: "5 AM",
                                         6: "6 AM",
                                         7: "7 AM",
                                         8: "8 AM",
                                         9: "9 AM",
                                         10: "10 AM",
                                         11: "11 AM",
                                         12: "12 PM",
                                         13: "1 PM",
                                         14: "2 PM",
                                         15: "3 PM",
                                         16: "4 PM",
                                         17: "5 PM",
                                         18: "6 PM",
                                         19: "7 PM",
                                         20: "8 PM",
                                         21: "9 PM",
                                         22: "10 PM",
                                         23: "11 PM", })

# Creates the graph
ax = analysis.plot(kind='bar', title='Crime over the Day')
ax.set_xlabel("Time of Day", fontsize=12)
ax.set_ylabel("Number of Crimes", fontsize=12)
ax.set_xticklabels(analysis['Time'], rotation=-45, fontsize=7, ha='left')
plt.show()
