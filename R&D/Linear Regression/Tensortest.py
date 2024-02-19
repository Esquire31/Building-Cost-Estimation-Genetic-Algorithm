import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
import pickle

fileList = ["Ceiling", "External_Wall", "Internal_Wall", "Floor", "Foundation_system", "Structure", "Structure", "Changes", "Duration", "Earthwork", "Escalation", "Floors", "Parking"]
sum = 0


def myfunc(x):
    return (slope * x + intercept)*0.9


value = int(input("Enter val: "))
for i in range(0, len(fileList)):
    filename = fileList[i]
    with open(f"models//{filename}.pkl", 'rb') as f:
        dataset = pickle.load(f)
        f.close()

    slope = dataset[0]
    intercept = dataset[1]

    prediction = myfunc(value)
    sum += prediction

print("The predicted value is: ", sum)
