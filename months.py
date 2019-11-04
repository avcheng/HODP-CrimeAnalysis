import pandas as pd
import geopy
from math import cos, asin, sqrt

data1 = pd.read_csv("Crime Log Data - Logs.csv")

temp = {}

for index, row in data1.iterrows():
    if (row['Date'])[-1] == '9' and ((row['Date'])[0:2] == '01' or (row['Date'])[0:2] == '02' or (row['Date'])[0:2] == '03' or (row['Date'])[0:2] == '04'):
        if((row['Date'])[0:2] in temp):
            temp[(row['Date'])[0:2]] +=1
        else:
            temp[(row['Date'])[0:2]] =1
    else:
        if (row['Date'])[-1] == '8' and ((row['Date'])[0:2] == '05' or (row['Date'])[0:2] == '06' or (row['Date'])[0:2] == '07' or (row['Date'])[0:2] == '08' or (row['Date'])[0:2] == '09' or (row['Date'])[0:2] == '10' or (row['Date'])[0:2] == '11' or (row['Date'])[0:2] == '12'):
            if((row['Date'])[0:2] in temp):
                temp[(row['Date'])[0:2]] +=1
            else:
                temp[(row['Date'])[0:2]] =1

print(temp)
