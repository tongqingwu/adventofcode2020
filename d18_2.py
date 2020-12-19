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

    if len(parsed) == 1:
        return interpreter(parsed[0])

    if parsed[0] == '*':
        return interpreter(parsed[1]) * sum(map(lambda x: interpreter(x), parsed[2:]))

    else:
        return sum(map(lambda x: interpreter(x), parsed))


def parser(line):
    line = line.replace(" ", "")

    # if just a number, return the string number
    if len(line) == 1:
        return [line] # e.g. ['7']

    # if no parentheses, and multiplication operator
    elif line[-1] != ")" and line[-2] == "*":
        return [line[-2], [parser(line[:-2])], parser(line[-1])]  # 3+5*2 -> ['*', [3+5], 2] -> ['*', [['3', '5']], 2]

    # if no parentheses and addition operator
    elif line[-1] != ")" and line[-2] == "+":
        return parser(line[:-2]) + [line[-1]]   # 8*4*2+3 -> [8*4*2, '3'] -> ['*', [['*', ['8'], '4']], '2', '3']

    # 8+4*2+3 -> [8+4*2, '3'] -> ['*', [8+4], '2', '3'] -> ['*', [['8', '4']], '2', '3']

    elif line[-1] == ")":
        start = find_bound(line)

        # if one parentheses object
        if start == 0:
            return [parser(line[1:-1])]   # e.g. (5+(3*2)) -> 5+(3*2)

        # parentheses with multiple objects
        elif line[start-1] == '*':
            return [line[start-1], [parser(line[:(start-1)])], parser(line[start:])]
            # e.g. (3*6)*(2+3) -> ['*', '(3*6)', '(2+3)']

        elif line[start-1] == '+':
            return parser(line[:(start - 1)]) + parser(line[start:])

f_name = sys.argv[1]
print(solution(f_name))
