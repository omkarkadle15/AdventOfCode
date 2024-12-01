import csv

sum_of_diff = 0
csv_file = open('location_ids.csv','r')
listA = []
listB = []
diff_list = []

for a, b in csv.reader(csv_file, delimiter=','):
    listA.append(int(a))
    listB.append(int(b))

listA.sort()
listB.sort()

len = len(listA)
for i in range(len):
    diff = abs(listA[i]-listB[i])
    diff_list.append(diff)

for x in diff_list:
    sum_of_diff = sum_of_diff + x

print(sum_of_diff)