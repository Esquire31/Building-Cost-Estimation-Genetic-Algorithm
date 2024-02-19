import pandas as pd
import csv

Nominals = ["Ceiling", "External_Wall", "Internal_Wall", "Floor", "Foundation_system", "Superstructure", "Substructure","Form_system"]
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

    unique_set = list(set(range))
    if len(unique_set)==3:
        count = 0
        while count!=length-1:
            count+=1
            i = count
            if range[i]==unique_set[0]:
                range[i]=1.0
            elif range[i]==unique_set[1]:
                range[i]=2.0
            elif range[i]==unique_set[2]:
                range[i]=3.0
            area[i]=area[i]/10000
            cost[i]=cost[i]/1000000
            final.append([area[i],range[i],cost[i]])
        with open(f"Datasets//Final_Modified_Data//{filename}.csv", 'r') as f:
            dataset = csv.reader(f)
            header = next(dataset)
        f.close()
        with open(f"Datasets//Encoded_Training_Data//Nominal//{filename}.csv", 'w') as f:
            csvwriter = csv.writer(f)
            csvwriter.writerow(header)
            csvwriter.writerows(final)
        f.close()
        value_data = f"{filename}:\n{unique_set[0]}: 1.0\n{unique_set[1]}: 2.0\n{unique_set[2]}: 3.0\n\n"
        with open("metadata.txt","a+") as f:
            f.writelines(value_data)
        f.close()
    
    if len(unique_set)==2:
        count = 0
        while count!=length-1:
            count+=1
            i = count
            if range[i]==unique_set[0]:
                range[i]=1.0
            elif range[i]==unique_set[1]:
                range[i]=2.0
            area[i]=area[i]/10000
            cost[i]=cost[i]/1000000
            final.append([area[i],range[i],cost[i]])
        with open(f"Datasets//Final_Modified_Data//{filename}.csv", 'r') as f:
            dataset = csv.reader(f)
            header = next(dataset)
        f.close()
        with open(f"Datasets//Encoded_Training_Data//Nominal//{filename}.csv", 'w') as f:
            csvwriter = csv.writer(f)
            csvwriter.writerow(header)
            csvwriter.writerows(final)
        f.close()
        value_data = f"{filename}:\n{unique_set[0]}: 1.0\n{unique_set[1]}: 2.0\n\n"
        with open("metadata.txt","a+") as f:
            f.writelines(value_data)
        f.close()
    
    if len(unique_set)==1:
        count = 0
        while count!=length-1:
            count+=1
            i = count
            if range[i]==unique_set[0]:
                range[i]=1.0
            area[i]=area[i]/10000
            cost[i]=cost[i]/1000000
            final.append([area[i],range[i],cost[i]])
        with open(f"Datasets//Final_Modified_Data//{filename}.csv", 'r') as f:
            dataset = csv.reader(f)
            header = next(dataset)
        f.close()
        with open(f"Datasets//Encoded_Training_Data//Nominal//{filename}.csv", 'w') as f:
            csvwriter = csv.writer(f)
            csvwriter.writerow(header)
            csvwriter.writerows(final)
        f.close()
        value_data = f"{filename}:\n{unique_set[0]}: 1.0\n\n"
        with open("metadata.txt","a+") as f:
            f.writelines(value_data)
        f.close()


for i in range(0,len(Nominals)):
    remodel(Nominals[i])