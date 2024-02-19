import csv
import numpy as np

data_set = []
test = []
with open(f"Datasets//Encoded_Training_Data//All//Final_Dataset.csv", 'r') as f:
    dataset = csv.reader(f)
    header = next(dataset)
    for row in dataset:
        data_set.append(row)
f.close()

original = len(data_set)

for i in range(0,len(data_set)):
    if len(test)>0:
        for j in range(0,len(test)):
            if data_set[i] not in test:
                test.append(data_set[i])
                with open("checkpoint.csv","a+") as f:
                    csvwriter = csv.writer(f)
                    csvwriter.writerows([data_set[i]])
                f.close()
                break
    else:
        test.append(data_set[i])

dup = len(test)
print(original,dup)