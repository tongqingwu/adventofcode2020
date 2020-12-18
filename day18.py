import re


def cal_all(input):
    sum_all = 0
    cnt = 0
    with open(input) as f:
        for line in f:
            cnt += 1
            line = line.rstrip()
            r = int(remove_p(line))
            # print('line {}: {} sum {}'.format(cnt, line, r))
            print('line {}: r = {}'.format(cnt, r))
            sum_all = sum_all + r

    print('cnt {}'.format(cnt))
    print('All sum {}'.format(sum_all))


def remove_p(line):
    line = cal_inside_p(line)
    while ' ' in line:
        line = cal_inside_p(line)
    return line


def cal_inside_p(line):
    m = re.search(r'(\d+ \S \d+)', line)
    if m:
        in_order_in = m.group(1)
        in_order_out = cal_first(in_order_in)
        line = line.replace(in_order_in, in_order_out)
        line = line.replace('(' + in_order_out + ')', in_order_out)
    return line


def cal_first(line):
    m = re.search(r'^(\d+) (\S) (\d+)', line)
    if m:
        n1 = m.group(1)
        op = m.group(2)
        n2 = m.group(3)

        first_pair = ' '.join([n1, op, n2])

        if op == '*':
            first = int(n1) * int(n2)
        elif op == '+':
            first = int(n1) + int(n2)
        else:
            print('Bad op')
            exit(1)

        extra = line.replace(first_pair, '')
        if extra:
            line = str(first) + extra
        else:
            line = str(first)

    return line


# def cal_in_order(line):
#     line = cal_first(line)
#     while ' ' in line:
#         line = cal_first(line)
#     return line


def main():
    line = '1 + 2 * 3 + 4 * 5 + 6'
    print('{}'.format(int(remove_p(line))))
    # cal_all('day18.txt')


if __name__ == '__main__':
    main()
