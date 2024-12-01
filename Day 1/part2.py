import csv

csv_file = open('location_ids.csv','r')
listA = []
listB = []
sim_score = []

for a, b in csv.reader(csv_file, delimiter=','):
    listA.append(int(a))
    listB.append(int(b))

len = len(listA)

for i in range(len):
    a = listA[i]
    c = 0
    for j in range(len):
        if a == listB[j]:
            c += 1
    prod = a * c
    sim_score.append(int(prod))

sum = 0
for x in sim_score:
    sum = sum + x

print(sum)