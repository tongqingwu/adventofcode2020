import re


def run_programs_part2(input_f):
    d_mem = dict()
    with open(input_f) as f:
        for line in f:
            line = line.rstrip()
            d = re.search(r'^mask = (.+)', line)
            m = re.search(r'^mem\[(\d+)\] = (\d+)', line)
            if d:
                mask = d.group(1)
            elif m:
                addr = int(m.group(1))
                data = int(m.group(2))

                mem_addrs = get_addrs(addr, mask)
                for b in mem_addrs:
                    d_mem[int(b, 2)] = data

    sum = add_data(d_mem)
    print('Part two: {}'.format(sum))


def get_addrs(data, mask):
    bin_data = '{:0>36b}'.format(data)

    l_addrs = []
    for i in range(36):
        l_addrs = get_new_list(l_addrs, mask[i], bin_data[i])

    return l_addrs


def get_new_list(old_l, mask, b):
    new_l = []
    if len(old_l) == 0:
        if mask == '0':
            new_l.append(b)
        elif mask == '1':
            new_l.append('1')
        elif mask == 'X':
            new_l.append('1')
            new_l.append('0')
    else:
        for ad in old_l:
            if mask == '0':
                new_l.append(ad + b)
            elif mask == '1':
                new_l.append(ad + '1')
            elif mask == 'X':
                new_l.append(ad + '1')
                new_l.append(ad + '0')

    return new_l


def run_programs(input_f):
    d_mem = dict()
    with open(input_f) as f:
        for line in f:
            line = line.rstrip()
            d = re.search(r'^mask = (.+)', line)
            m = re.search(r'^mem\[(\d+)\] = (\d+)', line)
            if d:
                mask = d.group(1)
            elif m:
                addr = int(m.group(1))
                data = int(m.group(2))
                d_mem[addr] = and_mask(data, mask)
                
    sum = add_data(d_mem)
    print('Part one: {}'.format(sum))


def and_mask(data, mask):
    bin_data = '{:0>36b}'.format(data)

    l_d = list(bin_data)
    for i in range(36):
        if mask[i] != 'X':
            l_d[i] = mask[i]

    bin_data = ''.join(l_d)
    new_data = int(bin_data, 2) 
    return new_data 


def add_data(d_mem):
    sum = 0
    for k, v in d_mem.items():
        if v != 0:
            sum += v

    return sum


def main():
    run_programs('day14.txt')
    run_programs_part2('day14.txt')


if __name__ == '__main__':
    main()
