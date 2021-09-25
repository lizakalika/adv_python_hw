import csv

with open("table.csv", "r") as file:
    r = csv.reader(file,delimiter=';') 
    data = []
    for row in r:
        data.append(row)
data.insert(4,[0,0,0,0,0,0])
for i in range(len(data)):
    data[i].insert(4,0)
#print(data)

with open("new_table.csv", "w") as file:
    writer = csv.writer(file)  
    writer.writerows(data)
