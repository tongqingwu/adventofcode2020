import re

PLUS = '+'
MULT = '*'


def cal_all(input):
    sum_all = 0
    cnt = 0
    with open(input) as f:
        for line in f:
            cnt += 1
            line = line.rstrip()
            line = line.replace(' ', '')
            if '(' in line:
                r = int(remove_p(line))
            else:
                r = int(cal_in_order(line))

            print('line {}: r = {}    line: >{}'.format(cnt, r, line))
            sum_all = sum_all + r

    print('cnt {}'.format(cnt))
    print('All sum {}'.format(sum_all))


def remove_p(line):
    line = cal_inside_p(line)
    while '(' in line:
        line = cal_inside_p(line)

    line = cal_in_order(line)  # without '(' now
    return line


def cal_inside_p(line):
    m = re.search(r'(\([+*0-9]*\))', line)
    if m:
        in_order_in = m.group(1)
        in_o = in_order_in.replace('(', '').replace(')', '')
        in_order_out = cal_in_order(in_o)
        line = line.replace(in_order_in, in_order_out)
    return line


def cal_first(line):
    m = re.search(r'^(\d+)(\D)(\d+)', line)
    n = re.search(r'^(\d+)(\D)(\d+)(\D.+)', line)
    ot = ''
    if n:
        n1 = n.group(1)
        op = n.group(2)
        n2 = n.group(3)
        ot = n.group(4)
    elif m:
        n1 = m.group(1)
        op = m.group(2)
        n2 = m.group(3)
    else:
        print('!!!! no match !!!!')

    if op == MULT:
        first = int(n1) * int(n2)
    elif op == PLUS:
        first = int(n1) + int(n2)

    line = str(first) + ot

    return line


def cal_in_order(line):
    line = cal_first(line)
    while re.search(r'^(\d+)([*+])(\d+)', line):
        line = cal_first(line)
    return line


def main():
    # line = '2*9+3*((3*7*4*3+3*8)*(8+6+3*8+6)+5+3+7+5)+9*(3+3+6+4)'
    # print('{}'.format(int(remove_p(line))))
    cal_all('day18.txt')


if __name__ == '__main__':
    main()
    # todo: how to debug when all examples passed?
