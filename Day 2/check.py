import csv

def main():
    with open('D:/Advent Of Code/Day 2/test.csv') as f:
        r = csv.reader(f)
        safe_count = 0
        for row in r:
            row = list(map(int, row))
            if isOrdered(row) == True and checkSafe(row) == True:
                print(f"{row} is a safe report")
                safe_count += 1
            else:
                print(f"rejecting {row}")
        print (f"The number of safe reports are: {safe_count}")


def isOrdered(input):
    if input == sorted(input):
        print(f"{input} is in ascending order")
        return True
    elif input == sorted(input, reverse=True):
        print(f"{input} is in descending order")
        return True
    else:
        print(f"{input} is not sorted, therefore it will be rejected")
        return False


def checkSafe(input):
    for index in range(1, len(input)):
        diff = abs(int(input[index])-int(input[index-1]))
        if 0 < diff <= 3:
            print(f"The difference between {input[index]} and {input[index - 1]} is {diff}")
            continue
        else:
            print(f"The difference between {input[index]} and {input[index - 1]} is {diff} which is unsafe, therefore {input} will be rejected")
            return False
    return True


if __name__ == "__main__":
    main()