import re


def get_schedule(input_f):
    with open(input_f) as f:
        for line in f:
            line = line.rstrip()
            d = re.search(r'\d+.+\,', line)
            if d:
                bus_list = line.split(',')
    return bus_list


def match_any_bus_dep_time(first_bus, dict_bus):
    timestamp = 0 
    while True:
        timestamp += first_bus 
        if count_true(timestamp, dict_bus):
           break

    return timestamp 


def count_true(timestamp, dict_bus):
    cnt = len(dict_bus)
    true_cnt = 0
    for k, v in dict_bus.items():
        if timestamp > k and (timestamp + v) % k == 0:
            true_cnt += 1
        else:
            return False

    if len(dict_bus) == true_cnt:
        return True
    else:
        return False
   
    
def main():
    b_list = get_schedule('day13.txt')
#    b_list = get_schedule('d13.txt')
    # b_list = ['17','x','13','19']
    # b_list = ['1789','37','47','1889']
    print(b_list)
    # get all D for all bus:
    first_bus = int(b_list[0])
    dict_bus = dict()
    for d in range(len(b_list)):
        bus_str = b_list[d]
        if d > 0 and bus_str != 'x': 
            dict_bus[int(bus_str)] = d 

    tsp = match_any_bus_dep_time(first_bus, dict_bus)

    print('Part two: {}'.format(tsp))


if __name__ == '__main__':
    main()

