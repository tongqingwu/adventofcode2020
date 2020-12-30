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


def cal_plus_first(line):
    m = re.search(r'^(\d+)\+(\d+)$', line)
    mm = re.search(r'^(\d+)\+(\d+)(\D.+)$', line)
    n = re.search(r'^([0-9*]*\*)(\d+)\+(\d+)$', line)
    nn = re.search(r'^([0-9*]*\*)(\d+)\+(\d+)(\D.+)$', line)
    mu = re.search(r'^(\d+)\*(\d+)$', line)
    muu = re.search(r'^(\d+)\*(\d+)(\*([0-9*]*))$', line)

    if mm:
        n1 = mm.group(1)
        n2 = mm.group(2)
        return str(int(n1) + int(n2)) + mm.group(3)
    elif nn:
        n1 = nn.group(2)
        n2 = nn.group(3)
        return nn.group(1) + str(int(n1) + int(n2)) + nn.group(4)
    elif n:
        n1 = n.group(2)
        n2 = n.group(3)
        return n.group(1) + str(int(n1) + int(n2))
    elif m:
        n1 = m.group(1)
        n2 = m.group(2)
        return str(int(n1) + int(n2))
    elif muu:
        n1 = muu.group(1)
        n2 = muu.group(2)
        return str(int(n1) * int(n2)) + muu.group(3)
    elif mu:
        n1 = mu.group(1)
        n2 = mu.group(2)
        return str(int(n1) * int(n2))
    else:
        print('!!!! no match !
        
    return line


def cal_in_order(line):
    line = cal_plus_first(line)
    while re.search(r'^(\d+)([*+])(\d+)', line):
        line = cal_plus_first(line)
    return line


def main():
    # line = '6*((4*8+4)+(3*5+3+3*7*5))+7+(9*(6+9*7+2*6*6))+2'
    # print('{}'.format(int(remove_p(line))))
    cal_all('day18.txt')


if __name__ == '__main__':
    main()
