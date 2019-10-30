import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("crime_data_log.csv")
# print(df.head())

include = ['Day of Week', 'Type']
analysis = df[include]

# print(analysis.head())

day = int(input("What day are you looking for?"))
analysis = analysis[analysis["Day of Week"] == day]
# print(analysis.head())

analysis = analysis['Type'].value_counts().reset_index().rename(columns={'index': 'Type', 'Type': 'Count'})
analysis['Count'] = pd.to_numeric(analysis['Count'])

analysis['Count'] = analysis['Count'] * 100 / analysis['Count'].sum()
analysis = analysis.head(10)
print(analysis)

ax = analysis.plot(kind='bar', title ="Crime")
ax.set_xlabel("Type", fontsize=12)
ax.set_ylabel("Rate as %", fontsize=12)
plt.show()
