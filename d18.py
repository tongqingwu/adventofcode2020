import sys

def solution(filename):
    f = open("./inputs/" + filename, 'r')
    f = f.read().split("\n")

    ans = 0
    for row in f:
        ans += interpreter(parser(row))

    return ans

def find_bound(line):
    count = 1
    for i in range(len(line)-2, -1, -1):
        if line[i] == ")":
            count += 1
        elif line[i] == "(":
            count -= 1
            if count == 0:
                return i

def interpreter(parsed):
    if type(parsed) is not list:
        return int(parsed)

    if parsed[0] == '*':
        return interpreter(parsed[1]) * interpreter(parsed[2])

    if parsed[0] == "+":
        return interpreter(parsed[1]) + interpreter(parsed[2])

def parser(line):
    line = line.replace(" ", "")

    # if just a number, return the string number
    if len(line) == 1:
        return line # e.g. 7

    # if no parentheses, return operator object
    elif line[-1] != ")":
        return [line[-2], parser(line[-1]), parser(line[:-2])]  # e.g. ['*', '2', '((6+2)*3)']

    elif line[-1] == ")":
        start = find_bound(line)

        # if one parentheses object
        if start == 0:
            return parser(line[1:-1])   # e.g. (5+(3*2)) -> 5+(3*2)

        # parentheses with multiple objects
        else:
            return [line[start-1], parser(line[start:]), parser(line[:(start-1)])]
            # e.g. (3*6)*(2+3) -> ['*', '(2+3)', '(3*6)']

f_name = sys.argv[1]
print(solution(f_name))

