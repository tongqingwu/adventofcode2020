import re


def get_schedule(input_f):
    with open(input_f) as f:
        for line in f:
            line = line.rstrip()
            d = re.search(r'\d+.+\,', line)
            if d:
                bus_list = line.split(',')
    return bus_list


def find_ts(dict_bus):
    l_bus = sorted(dict_bus.keys(), reverse=True)
    print('After sort, bus list {}'.format(l_bus))

    ts = 0
    num = 0
    mod = 0
    next_num = 0
    next_mod = 0
    for d in range(len(l_bus) - 1):
        print('D ----- {}'.format(d))
        bus = l_bus[d]
        next_bus = l_bus[d + 1]
        next_num = dict_bus[next_bus]
        if d == 0:
            num = dict_bus[bus]
            mod = bus
        else:
            num = ts
            mod = lcm(bus, mod)

        ts = get_ts_by_pair(num, mod, next_num, next_bus)

    return ts


def get_ts_by_pair(num, mod, next_num, next_mod):
    print('num {}, mod {}, next num {}, next mod {}'.format(num, mod, next_num, next_mod))
    ts = 0
    m = 0
    while True:
        ts = mod * m + num
        if ts % next_mod == next_num:
            break
        m += 1

    return ts


def lcm(n1, n2):
    z = n1 if n1 > n2 else n2

    while z % n1 != 0 or z % n2 != 0:
        z += 1
    return z
   
    
def main():
    b_list = get_schedule('day13.txt')
    # b_list = get_schedule('d13.txt')
    # b_list = ['17','x','13','19']
    #b_list = ['1789','37','47','1889']
    # b_list = ['67','7','x','59','61']
    # b_list = ['67','x','7','59','61']
    print(b_list)

    dict_bus = dict()

    for d in range(len(b_list)):
        print('Bus d {} -----'.format(d))
        bus_str = b_list[d]
        if bus_str != 'x': 
            bus = int(bus_str)
            if d == 0:
                dict_bus[bus] = 0 
            else:
                diff = bus - d 
                if diff > 0: 
                   dict_bus[bus] = bus - d 
                else:
                   dict_bus[bus] = diff % bus 

    print('dict is {}'.format(dict_bus))

    ts = find_ts(dict_bus)

    print('Part two: {}'.format(ts))


if __name__ == '__main__':
    main()

