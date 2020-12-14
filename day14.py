import re


def run_programs(input_f):
    b_list = []
    d_mem = dict()
    with open(input_f) as f:
        for line in f:
            line = line.rstrip()
            d = re.search(r'^mask = (.+)', line)
            m = re.search(r'^mem\[(\d+)\] = (\d+)', line)
            if d:
                mask = d.group(1)
                print('mask: {}'.format(mask)) 
            elif m:
                addr = int(m.group(1))
                data = int(m.group(2))
                d_mem[addr] = and_mask(data, mask)
    return d_mem 


def and_mask(data, mask):
    print('data {} --------------'.format(data))
    print('mas: {}'.format(mask))
    bin_data = '{:0>36b}'.format(data)
    print('bin: {}'.format(bin_data))
    print(bin_data)

    l_d = list(bin_data)
    for i in range(36):
        if mask[i] != 'X':
            l_d[i] = mask[i]

    bin_data = ''.join(l_d)
    print('n_b: {}'.format(bin_data))
    new_data = int(bin_data, 2) 
    print('data {} to new data {}'.format(data, new_data))
    return new_data 


def add_data(d_mem):
    sum = 0
    for k, v in d_mem.items():
        print('m {}, d {}'.format(k, v))
        if v != 0:
            sum += v

    return sum


def main():
    sum = add_data(run_programs('day14.txt'))
    print('Part one: {}'.format(sum))


if __name__ == '__main__':
    main()

