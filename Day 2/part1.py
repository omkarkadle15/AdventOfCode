import csv 

unsafe_count = 0
with open('reports.csv') as f:
    r = csv.reader(f)
    for row in r:
        if row == sorted(row) or row == sorted(row, reverse=True):
            c = 0
            for i in range(1, len(row)):
                diff = abs(int(row[i])-int(row[i-1]))
                while c == 0:
                    if diff > 3 or diff == 0:
                        c += 1
                        unsafe_count += 1
                    break
        else:
            unsafe_count += 1

print(unsafe_count)