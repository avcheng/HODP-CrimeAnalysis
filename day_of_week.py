import pandas as pd
import matplotlib.pyplot as plt

# Imports and reads only day of week and type
df = pd.read_csv("crime_data_log.csv")
include = ['Day of Week', 'Type']
analysis = df[include]

# Specifies day of week that want to analyze
day = int(input("What day are you looking for?"))
analysis = analysis[analysis["Day of Week"] == day]

# Counts up each crime type and turns to percentage of crime that day
analysis = analysis['Type'].value_counts().reset_index().rename(columns={'index': 'Type', 'Type': 'Count'})
analysis['Count'] = pd.to_numeric(analysis['Count'])
analysis['Count'] = analysis['Count'] * 100 / analysis['Count'].sum()

# Chooses top ten crimes
analysis = analysis.head(10)

# Creates the graph
ax = analysis.plot(kind='bar', title ="Crime")
ax.set_xlabel("Type", fontsize=12)
ax.set_ylabel("Rate as %", fontsize=12)
ax.set_xticklabels(analysis['Type'], rotation=-60, fontsize=7, ha='left')
plt.show()
