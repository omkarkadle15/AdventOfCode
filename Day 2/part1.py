import csv

def main():
    with open('D:/Advent Of Code/Day 2/reports.csv') as f:
        r = csv.reader(f)
        safe_count = 0
        for row in r:
            if isAscendingOrDescending(row) == False or checkSafe(row) == False:
                continue
            else:
                safe_count += 1
        print(safe_count)


def isAscendingOrDescending(input):
    if input != sorted(input) and input != sorted(input, reverse=True):
        return False


def checkSafe(input):
    for index in range(1, len(input)):
        if abs(int(input[index])-int(input[index-1])) == 0 or abs(int(input[index])-int(input[index-1])) > 3:
            return False


if __name__ == "__main__":
    main()