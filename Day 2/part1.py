import csv

def main():
    with open('reports.csv') as f:
        r = csv.reader(f)
        safe_count = 0
        for row in r:
            row = list(map(int, row))
            if isOrdered(row) == True and checkSafe(row) == True:
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


def checkSafe(input):
    for index in range(1, len(input)):
        diff = abs(input[index] - input[index-1])
        if 0 < diff <= 3:
            continue
        else:
            return False
    return True


if __name__ == "__main__":
    main()