import pandas as pd
import matplotlib.pyplot as plt

# Imports and reads only day of week
df = pd.read_csv("crime_data_log.csv")
analysis = df['Day of Week']

# Counts up crime per day
analysis = analysis.value_counts().reset_index().rename(columns={'index': 'Day of Week',
                                                                 'Day of Week': 'Count'})
analysis = analysis.sort_values(by='Day of Week')
analysis['Day of Week'] = analysis['Day of Week'].map({0: "Sunday",
                                        1: "Monday",
                                        2: "Tuesday",
                                        3: "Wednesday",
                                        4: "Thursday",
                                        5: "Friday",
                                        6: "Saturday"})

# Creates the graph
ax = analysis.plot(kind='bar', title='Crime over the Week')
ax.set_xlabel("Day of the Week", fontsize=12)
ax.set_ylabel("Number of Crimes", fontsize=12)
ax.set_xticklabels(analysis['Day of Week'], rotation=0, fontsize=7)
plt.show()
