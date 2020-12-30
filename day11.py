E = 'L'
O = '#'
F = '.'
seats_rows = 0
seats_cols = 0


def show_seats(seats):
    for row in seats:
        print(row)


def part(seats, part2=False):
    cnt = 1
    state_change_cnt, new_seats, occupied_cnt = get_new_seats(seats, part2=part2)
    # show_seats(new_seats)
    print('Round {}: state change cnt {}, occupied_cnt {}'.format(cnt, state_change_cnt, occupied_cnt))

    while state_change_cnt > 0:
        cnt += 1
        state_change_cnt, new_seats, occupied_cnt = get_new_seats(new_seats, part2=part2)
        # show_seats(new_seats)
        print('Round {}: state change cnt {}, occupied_cnt {}'.format(cnt, state_change_cnt, occupied_cnt))


def get_new_seats(seats, part2=False):
    # return state_change_cnt and new seats
    global seats_rows
    global seats_cols
    seats_rows = len(seats)
    seats_cols = len(seats[0])
    state_change_cnt = 0
    occupied_cnt = 0
    new_seats = []
    for row in range(seats_rows):
        tmp_row = ''
        for col in range(seats_cols):
            if part2:
                new_status = get_new_status_part2(seats, row, col)
            else:
                new_status = get_new_status(seats, row, col)
            if new_status != seats[row][col]:
                state_change_cnt += 1
            if new_status == O:
                occupied_cnt += 1
            tmp_row += new_status
        new_seats.append(tmp_row)
    return state_change_cnt, new_seats, occupied_cnt


def adj_status(seats, row, col, relative_position):
    global seats_rows
    global seats_cols
    n_col = col
    n_row = row
    status = F

    if 'left' in relative_position:
        n_col = col - 1
    elif 'right' in relative_position:
        n_col = col + 1

    if 'up' in relative_position:
        n_row = row - 1
    elif 'down' in relative_position:
        n_row = row + 1

    if 0 <= n_col < seats_cols and 0 <= n_row < seats_rows:
        status = seats[n_row][n_col]
        
    return status


def adj_status_part2(seats, row, col, relative_position):
    global seats_rows
    global seats_cols
    n_col = col
    n_row = row
    status = F

    if 'left' == relative_position:
        n_col = col - 1
        while status == F and n_col > -1:
            status = seats[n_row][n_col]
            n_col -= 1
    elif 'right' == relative_position:
        n_col = col + 1
        while status == F and n_col < seats_cols:
            status = seats[n_row][n_col]
            n_col += 1
    elif 'up' == relative_position:
        n_row = row - 1
        while status == F and n_row > -1:
            status = seats[n_row][n_col]
            n_row -= 1
    elif 'down' == relative_position:
        n_row = row + 1
        while status == F and n_row < seats_rows:
            status = seats[n_row][n_col]
            n_row += 1
    elif 'left_up' == relative_position:
        n_col = col - 1
        n_row = row - 1
        while status == F and n_col > -1 and n_row > -1:
            status = seats[n_row][n_col]
            n_col -= 1
            n_row -= 1
    elif 'right_up' == relative_position:
        n_col = col + 1
        n_row = row - 1
        while status == F and n_col < seats_cols and n_row > -1:
            status = seats[n_row][n_col]
            n_col += 1
            n_row -= 1
    elif 'left_down' == relative_position:
        n_col = col - 1
        n_row = row + 1
        while status == F and n_col > -1 and n_row < seats_rows:
            status = seats[n_row][n_col]
            n_col -= 1
            n_row += 1
    elif 'right_down' == relative_position:
        n_row = row + 1
        n_col = col + 1
        while status == F and n_row < seats_rows and n_col < seats_cols:
            status = seats[n_row][n_col]
            n_row += 1
            n_col += 1

    return status

    
def get_new_status_part2(seats, row, col):
    # check_rules 
    # return new status
    is_occupied_cnt = 0
    own_status = seats[row][col]
    if own_status == F:
        return F

    for pos in ['left', 'left_up', 'left_down', 'right', 'right_up', 'right_down', 'up', 'down']:
        if adj_status_part2(seats, row, col, pos) == O:
            is_occupied_cnt += 1

    if is_occupied_cnt == 0 and own_status == E:
        # print('Find E, other E')
        return O

    if (is_occupied_cnt == 5 or is_occupied_cnt > 5) and own_status == O:
        # print('Find O, other 4 O')
        return E

    return own_status


def get_new_status(seats, row, col):
    # check_rules 
    # return new status
    is_occupied_cnt = 0
    own_status = seats[row][col]
    if own_status == F:
        return F

    for pos in ['left', 'left_up', 'left_down', 'right', 'right_up', 'right_down', 'up', 'down']:
        if adj_status(seats, row, col, pos) == O:
            is_occupied_cnt += 1

    if is_occupied_cnt == 0 and own_status == E:
        return O

    if (is_occupied_cnt == 4 or is_occupied_cnt > 4) and own_status == O:
        return E

    return own_status


def get_seats_from_file(f_name):
    seats = []
    with open(f_name) as f:
        for line in f:
            line = line.rstrip()
            seats.append(line)

    return seats


def main():
    global seats_rows
    global seats_cols
    seats = get_seats_from_file('day11.txt')
    seats_rows = len(seats)
    seats_cols = len(seats[0])

    # part 1:
    print('Part one:')
    part(seats)
    print('Part two:')
    part(seats, part2=True)


if __name__ == '__main__':
    main()
