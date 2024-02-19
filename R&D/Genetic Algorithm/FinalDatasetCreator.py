import pandas as pd
import csv
import random

global headers
def generate():
    global headers
    fileList = ["Ceiling", "External_Wall", "Internal_Wall", "Floor", "Foundation_system", "Form_system", "Superstructure", "Substructure", "Changes", "Duration", "Earthwork", "Floors", "Parking","Escalations"]
    headers = []
    sum = 0
    values = []

    for i in range(0,len(fileList)):
        filename = fileList[i]
        data = pd.read_csv(rf"Datasets/Encoded_Training_Data/All/{filename}.csv")

        area = list(data.AREA)
        ranges = list(data.RANGE)
        cost = list(data.EC)

        rows = []

        with open(f"Datasets//Encoded_Training_Data//All//{filename}.csv", 'r') as f:
            dataset = csv.reader(f)
            header = next(dataset)
            for row in dataset:
                rows.append(row)
        f.close()
        if i==0:
            area_choice = random.choice(rows)
            sum+=float(area_choice[2])
            headers.append("AREA")
            headers.append(f"{filename}.RANGE")
            values.append(area_choice[0])
            values.append(area_choice[1])
        else:
            while 1:
                random_choice = random.choice(rows)
                if area_choice[0]==random_choice[0]:
                    headers.append(f"{filename}.RANGE")
                    sum+=float(random_choice[2])
                    values.append(random_choice[1])
                    break
                else:
                    pass
    values.append(sum)
    headers.append("Total_Cost")
    return values

limit_file = pd.read_csv(rf"Datasets/Encoded_Training_Data/All/Minmax.csv")
min_value = limit_file.LCOST
max_value = limit_file.HCOST
area_val = limit_file.AREA

data_set = []
with open(f"Datasets//Encoded_Training_Data//All//Final_Dataset.csv", 'r') as f:
    dataset = csv.reader(f)
    header = next(dataset)
    for row in dataset:
        data_set.append(row)
f.close()

for i in range(0,200):
    output = generate()
    output[0] = float(output[0])
    for j in range(0,len(area_val)):
        val_area = float(area_val[j]/10000)
        if output[0]==val_area:
            if output[-1]<(max_value[j]/1000000) and output[-1]>(min_value[j]/1000000):
                if output not in data_set:
                    with open(f"Datasets//Encoded_Training_Data//All//Final_Dataset.csv", 'a+') as f:
                        csvwriter = csv.writer(f)
                        csvwriter.writerows([output])
                    f.close()
                    print(len(data_set))
            else:
                break

