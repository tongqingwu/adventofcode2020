import re


def get_schedule(input_f):
    b_list = []
    with open(input_f) as f:
        for line in f:
            line = line.rstrip()
            d = re.search(r'^(\d+)$', line)
            if d:
                timestamp_start = int(d.group(1))
                print('Start at: {}'.format(timestamp_start)) 
            else:
                bus_list = line.split(',')
                bus_list = list(set(bus_list))
                bus_list.remove('x')
                for b in bus_list:
                    b_list.append(int(b))
                b_list.sort()
                print(b_list)
    return timestamp_start, b_list


def main():
    start_ts, b_list = get_schedule('day13.txt')
    #start_ts, b_list = get_schedule('d13.txt')
    # get all D for all bus:
    earliest = b_list[-1] 
    print('e is {}'.format(earliest))
    m = 0
    for b in b_list:
        e_diff = b - (start_ts % b)
        if e_diff < earliest:
            earliest = e_diff 
            m = earliest * b

    print('Part one: {}'.format(m))


if __name__ == '__main__':
    main()

