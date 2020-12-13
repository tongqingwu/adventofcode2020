import re


def get_schedule(input_f):
    with open(input_f) as f:
        for line in f:
            line = line.rstrip()
            d = re.search(r'\d+.+\,', line)
            if d:
                bus_list = line.split(',')
    return bus_list


def match_any_bus_dep_time(first_bus, big_bus, dict_bus):
    timestamp = 0 
    print('big bus {} start from {}'.format(big_bus, timestamp))
    while True:
        timestamp += big_bus 
        if first_bus != big_bus:
            first_bus_ts = timestamp - dict_bus[big_bus]
        else:
            first_bus_ts = timestamp

        if count_true(first_bus, first_bus_ts, dict_bus):
           break

    print('time: {}'.format(timestamp))
    return first_bus_ts 


def count_true(first_bus, timestamp, dict_bus):
    if timestamp % first_bus != 0:
        return False
 
    cnt = len(dict_bus)
    true_cnt = 0
    for k, v in dict_bus.items():
        if (timestamp + v) % k == 0:
            true_cnt += 1
        else:
            print('TS {} not match bus {}'.format(timestamp, k))
            return False

    if len(dict_bus) == true_cnt:
        return True
    else:
        return False
   
    
def main():
    # b_list = get_schedule('day13.txt')
    # b_list = get_schedule('d13.txt')
    # b_list = ['17','x','13','19']
    # b_list = ['1789','37','47','1889']
    # b_list = ['67','7','x','59','61']
    b_list = ['67','x','7','59','61']
    print(b_list)
    # get all D for all bus:
    first_bus = int(b_list[0])
    big_bus = first_bus 
    dict_bus = dict()
    for d in range(len(b_list)):
        bus_str = b_list[d]
        if d > 0 and bus_str != 'x': 
            bus = int(bus_str)
            if bus > big_bus:
                big_bus = bus
            dict_bus[int(bus_str)] = d 

    print('big_bus {}'.format(big_bus))
    tsp = match_any_bus_dep_time(first_bus, big_bus, dict_bus)

    print('Part two: {}'.format(tsp))


if __name__ == '__main__':
    main()

