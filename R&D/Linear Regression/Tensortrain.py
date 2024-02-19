import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
import pickle

fileList = ["Ceiling", "External_Wall", "Internal_Wall", "Floor", "Foundation_system", "Structure", "Structure", "Changes", "Duration", "Earthwork", "Escalation", "Floors", "Parking"]

def namepass(filename):
    data = pd.read_csv(rf"Training_Data/{filename}.csv")

    x = data.AREA
    y = data.EC

    slope, intercept, r, p, std_err = stats.linregress(x, y)

    data = [slope,intercept]
    with open(f"models//{filename}.pkl",'wb') as f:
        dataset = pickle.dump(data,f)
        f.close()

for i in range(0,len(fileList)):
    namepass(fileList[i])