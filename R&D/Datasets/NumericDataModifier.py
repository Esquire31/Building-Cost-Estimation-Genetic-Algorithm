from ast import Num
import pandas as pd
import csv

Numericals = ["Duration", "Earthwork", "Floors", "Parking","Changes","Escalations"]
def remodel(filename):
    data = pd.read_csv(rf"Datasets/Final_Modified_Data/{filename}.csv")

    area = list(data.AREA)
    range = list(data.RANGE)
    cost = list(data.EC)

    final = []

    len_area = len(area)
    length = int(len_area)

    #Now we are encoding the training data for each variable 
    #Train the model in regression and see if we are getting desired outputs
    #If we get it, try the same data in genetic algorithm
    # Note: To be done for every variable and then get sum of all

    #HARD ENCODING:
    #AREA/10,000
    #COST/10,00,000

    count = 0
    while count!=length-1:
        count+=1
        i = count
        range[i]==float(range[i])
        area[i]=area[i]/10000
        cost[i]=cost[i]/1000000
        final.append([area[i],range[i],cost[i]])
    with open(f"Datasets//Final_Modified_Data//{filename}.csv", 'r') as f:
        dataset = csv.reader(f)
        header = next(dataset)
    f.close()
    with open(f"Datasets//Encoded_Training_Data//Numerical//{filename}.csv", 'w') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(header)
        csvwriter.writerows(final)
    f.close()

for i in range(0,len(Numericals)):
    remodel(Numericals[i])