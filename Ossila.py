import pandas as pd
import numpy as np
import csv

# fileName = input("Enter the name of the wavelength file: ")

# optical parameter
fileName = "Sample"
# ossila
fileName2 = "2026-01-30-Ossila Pixel 1 (2)"

# time between ossila cycles(min), optical parameter cycles should be 60s
ossilaCycle = 60

op = pd.read_csv(f'{fileName}.csv', skiprows=14)
sc = pd.read_csv(f'{fileName2}.csv')

# Date (MM/dd/yyyy) ,Time of day (hh:mm:ss)
time = []

# gives sun intensity
sunIntensity = []
for i in range(len(op)):
    # mW/cm^2
    x = op["Power (W)"].iloc[i] * 1000 / 0.785
    time.append((op["Date (MM/dd/yyyy) "].iloc[i], op["Time of day (hh:mm:ss) "].iloc[i]))

    sunIntensity.append(x)

# gives cell intensity
cellIntensity = []
for i in range(len(sc)):
    # mW/cm^2
    x = sc["Jsc (A.cm^-2)"].iloc[i] * sc["Voc (V)"].iloc[i] * sc["FF (%)"].iloc[i] / 100 * 1000

    print(abs(x))

    cellIntensity.append(abs(x))


data = [
    ["Date (MM/dd/yyyy)", "Time of day (hh:mm:ss)", "Jsc(mA/cm^2)", "Voc(V)", "FF(%)", "Pin(mW/cm^2)", "Pce"]
]

# averages data points of optical parameter measurments to get more accurate readings and gets true efficiency
for i in range(len(cellIntensity)):
    sunAverage = 0
    count = 1
    for j in range(count * ossilaCycle, count * ossilaCycle + ossilaCycle):
        try:
            sunAverage += sunIntensity[j]
        except:
            break

    count += 1
    
    sunAverage /= ossilaCycle

    # pce
    x = cellIntensity[i] / sunAverage * 100
    data.append([time[count * ossilaCycle][0],time[count * ossilaCycle][1],
                abs(sc["Jsc (A.cm^-2)"].iloc[i] * 1000), sc["Voc (V)"].iloc[i], sc["FF (%)"].iloc[i], 
                sunAverage, x])

csvFilePath = "EfficiencyMeasurements.csv"

with open(csvFilePath, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
