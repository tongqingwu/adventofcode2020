seat_dict = {} # {'0' : [1, 2, 3, 5 ...], '1': [126 ...]} key is row num value is column num array

def create_seat_dict():
    global seat_dict
    for i in range(1, 127):
        # print(i)
        seat_dict[i] = []


def get_seats():
    seats = []

    with open('day5.txt') as f:
        for line in f:
            line = line.strip()
            seats.append(line)
    print('Totol {} seats'.format(len(seats)))
    return seats


def get_highest_id(seats):
    id_highest = 0
    for s in seats:
        id = convert_seat_to_id(s)
        # print(id)
        if id > id_highest:
            id_highest = id

    return id_highest


def convert_seat_to_id(s):
    global seat_dict
    row = ''
    col = ''
    for i in range(7):
        row += s[i]

    for i in range(7, 10):
        col += s[i]

    # print(row)
    # print(col)

    row_num = get_last_element(128, row)
    col_num = get_last_element(8, col)

    seat_dict[row_num].append(col_num)

    # print('row {}'.format(row_num))
    if row_num == 0 or row_num == 127:
        print('not my seat')
    id = row_num * 8 + col_num
    # print(id)

    return id


def get_last_element(cnt, s):
    '''

    :param cnt: 8 or 128
    :param s: 'RLR', or 'FBFBBFF'
    :return:
    '''
    level = 0
    a = get_array(cnt)
    while len(a) > 1:
        a = separate_array(a, s[level])
        level = level + 1

    # print(a)
    return a[0]


def separate_array(a, fb):
    '''

    :param a: input array
    :return: two arrays
    '''
    a_len = len(a)
    half = int(a_len/2)
    # print('half {}'.format(half))
    a_half = []

    if fb == 'F' or fb == 'L':
        for i in range(half):
            a_half.append(a[i])
    if fb == 'B' or fb == 'R':
        for i in range(half, a_len):
            a_half.append(a[i])
    # print(a_half)

    return a_half


def get_array(cnt):
    a = []
    for i in range(cnt):
        a.append(i)

    return a


def find_my_seat():
    global seat_dict
    for k, v in seat_dict.items():
        print('cols in row {}:{}'.format(k, v))
        len_col = len(v)
        print('len v {}'.format(len_col))
        if len_col == 7:
            for i in range(0, 8):
                # print(i)
                if i not in v:
                    id = k * 8 + i
                    print('missing id {}'.format(id))
    return id


def main():
    create_seat_dict()
    h_id = get_highest_id(get_seats())
    print('Highest id {}'. format(h_id))

    print('missing id : {}'.format(find_my_seat()))



if __name__ == '__main__':
    main()
