import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
import csv


fileList = ["Ceiling", "External_Wall", "Internal_Wall", "Floor","Form_system","Foundation_system", "Superstructure", "Substructure", "Changes", "Duration", "Earthwork", "Floors", "Parking","Changes","Escalations"]

def namepass(name):
    rows = []
    filename = name
    with open(f"Datasets//Final_Recieved_Data//{filename}.csv", 'r') as f:
        dataset = csv.reader(f)
        header = next(dataset)
        for row in dataset:
            rows.append(row)
    f.close()
    for i in range(0,len(rows)):
        rows[i][2]=float(rows[i][2])
        rows[i][2] = 2.5*(rows[i][2]/5.3)
    with open(f"Datasets//Final_Modified_Data//{filename}.csv", 'w') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(header)
        csvwriter.writerows(rows)
        f.close()

for i in range(0,len(fileList)):
    namepass(fileList[i])