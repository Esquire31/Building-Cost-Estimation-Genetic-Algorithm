import csv

file = open('numerical.csv')
csvreader = csv.reader(file)

header = list()
header = next(csvreader)

rows = []
for row in csvreader:
    rows.append(row)

line = []
data = []
for i in range(len(rows)):
    if rows[i][1] == 'Duration_of_the_project':
        line.append(rows[i])
print(line)


filename = 'Duration.csv'
with open(filename, 'w', newline="") as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(header)
    csvwriter.writerows(line)
