def is_tree(string, index):
    if string[index] == '#':
        return True
    else:
        return False


def get_line_pass_index(line, index):
    out_line = line
    line_len = len(line)
    if index >= line_len:
        out_line = line * ( int(index / line_len) + 1)

    # print('Index {}, new len {}'.format(index, len(out_line)))
    return out_line


def get_tree_cnt_right_down(right, down):
    cnt = 0

    with open('day3.txt') as f:
        line_num = 0

        for line in f:
            line = line.strip()
            if line_num == 0:
                print('New line, skip {}'.format(line))
            else:
                if (line_num % down) == 0:
                    index = int(line_num / down) * right

                    out_line = get_line_pass_index(line, index)
                    if is_tree(out_line, index):
                        cnt = cnt + 1

            line_num = line_num + 1
    print(cnt)
    return cnt


def main():
    # part one:
    # print(get_tree_cnt_right_down_one(3))

    # part two:
    part2 = get_tree_cnt_right_down(1, 1) * \
            get_tree_cnt_right_down(3, 1) * \
            get_tree_cnt_right_down(5, 1) * \
            get_tree_cnt_right_down(7, 1) * \
            get_tree_cnt_right_down(1, 2)

    print(part2)


if __name__ == '__main__':
    main()

