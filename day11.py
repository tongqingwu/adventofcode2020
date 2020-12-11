E = 'L'
O = '#'
F = '.'
seats_rows = 0 
seats_cols = 0 


def show_seats(seats):
    for row in seats:
        print(row)


def part1(seats):
    cnt = 1
    state_change_cnt, new_seats, occupied_cnt = get_new_seats(seats) 
    # show_seats(new_seats)
    print('Round {}: state change cnt {}, occupied_cnt {}'.format(cnt, state_change_cnt, occupied_cnt))

    while state_change_cnt > 0:
        cnt += 1
        state_change_cnt, new_seats, occupied_cnt = get_new_seats(new_seats)
        # show_seats(new_seats)
        print('Round {}: state change cnt {}, occupied_cnt {}'.format(cnt, state_change_cnt, occupied_cnt))


def get_new_seats(seats):
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
            new_status = get_new_status(seats, row, col) 
            if new_status != seats[row][col]:
                # print('changed ....')
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

    if n_col >= 0 and n_row >= 0 and n_col < seats_cols and n_row < seats_rows: 
        status = seats[n_row][n_col]
    # print('{} status {}'.format(relative_position, status))
    return status


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
        # print('Find E, other E')
        return O

    if (is_occupied_cnt == 4 or is_occupied_cnt > 4) and own_status == O: 
        # print('Find O, other 4 O')
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
    part1(seats)


if __name__ == '__main__':
    main()





