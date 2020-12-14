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
        #        print('mask: {}'.format(mask)) 
            elif m:
                addr = int(m.group(1))
                data = int(m.group(2))
              
                mem_addrs = get_addrs(addr, mask)
                for b in mem_addrs:
                    d_mem[int(b, 2)] = data 

    sum = add_data(d_mem)
    print('Part two: {}'.format(sum))


def get_addrs(data, mask):
    # print('add {} --------------'.format(data))
    # print('mas: {}'.format(mask))
    bin_data = '{:0>36b}'.format(data)
    # print('bin: {}'.format(bin_data))

    l_addrs = []
    for i in range(36):
        l_addrs = get_new_list(l_addrs, mask[i], bin_data[i])
        # print('l_addrs {} after check {}'.format(l_addrs, i))

    # for a in l_addrs:
    #  print('mem: {}'.format(a))
    return l_addrs 


def get_new_list(old_l, mask, b):
    # print('----mask {}, b {}'.format(mask, b))
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
           # print('ad {}'.format(ad))
           if mask == '0':
              new_l.append(ad + b)
           elif mask == '1':
              new_l.append(ad + '1')
           elif mask == 'X':
              new_l.append(ad + '1')
              new_l.append(ad + '0')

    return new_l


def add_data(d_mem):
    sum = 0
    for k, v in d_mem.items():
        # print('m {}, d {}'.format(k, v))
        if v != 0:
            sum += v

    return sum


def main():
    # run_programs('d14_2.txt')
    run_programs('day14.txt')


if __name__ == '__main__':
    main()

