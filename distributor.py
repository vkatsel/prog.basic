import pickle
import os
data = []
groups = {}
with open(os.getcwd()+'\data.csv', 'r') as file:
    next(file)
    for row in file:
        row = [int(i) if i.isdigit() else i for i in row.split(', ')]
        data.append(row)
        if row[3] not in groups:
            groups[row[3]] = {}
        if row[5][:-1] not in groups[row[3]]:
            groups[row[3]][row[5][:-1]] = []

for student in data:
    groups[student[3]][student[5][:-1]].append([student[1], student[2], student[4]])

#groups = sorted(groups.items(), key=lambda x: x[0])

with open(os.getcwd()+'\groups.csv', 'wb') as file:
    data = pickle.dump(groups, file)








