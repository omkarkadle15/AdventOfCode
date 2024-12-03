import csv

def main():
    with open('D:/Advent Of Code/Day 2/reports.csv') as f:
        r = csv.reader(f)
        safe_count = 0
        for row in r:
            row = list(map(int, row))
            if isSafe(row) == True:
                safe_count += 1
            elif remIndex(row) == True:
                safe_count += 1
            else:
                continue
        print(f"The number of safe reports are: {safe_count}")


def isOrdered(input):
    if input == sorted(input):
        return True
    elif input == sorted(input, reverse=True):
        return True
    else:
        return False


def checkDiff(input):
    for index in range(1, len(input)):
        diff = abs(input[index] - input[index-1])
        if 0 < diff <= 3:
            continue
        else:
            return False
    return True


def remIndex(input):
    for index in range(len(input)):
        temp = list(input)
        temp.pop(index)
        if isSafe(temp) == False:
            continue
        else:
            return True
    return False


def isSafe(input):
    if isOrdered(input) == True and checkDiff(input) == True:
        return True
    else:
        return False


if __name__ == "__main__":
    main()