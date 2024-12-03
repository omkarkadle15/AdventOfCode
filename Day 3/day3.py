import re

def main():
    with open('input.txt') as f:
        txt = f.read()
        print(captureEx(txt))


def captureEx(txt):
    pattern = re.compile(r"mul\(([0-9],|[1-9][0-9],|[1-9][0-9][0-9],)([0-9]\)|[1-9][0-9]\)|[1-9][0-9][0-9]\))")
    sum = 0
    for match in pattern.finditer(txt):
        num1 = int(match.group(1).strip(','))
        num2 = int(match.group(2).strip(')'))
        product = num1 * num2
        sum = sum + product
    return sum


if __name__ == "__main__":
    main()