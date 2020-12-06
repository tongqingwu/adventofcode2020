
import re


def check_valid_pass(line, part1=True):
    print(line)
    is_valid = False
    d = re.search(r'(\d+)-(\d+) (\S): (\S+)', line)
    if d:
        cnt = 0
        at_least = int(d.group(1))
        at_most = int(d.group(2))
        letter = d.group(3)
        input_str = d.group(4)

        for i in range(0, len(input_str)):
            pos = i + 1

            if input_str[i] == letter:
                if input_str[i] == letter and (pos == at_least or pos == at_most):
                    print('pos {} - {}:{}, at_least {}, at_most {}'.format(pos, i, input_str[i], at_least, at_most))
                    cnt += 1
        if cnt == 1:
            is_valid = True
            print('Valid pass')
        else:
            print('cnt {}'.format(cnt))

        #
        #     if input_str[i] == letter:
        #         cnt += 1
        #
        # if int(at_most) >= cnt >= int(at_least):
        #     print("it is valid pass" + line)
        #     is_valid = True

    return is_valid


def main():
    total_cnt = 0

    with open('day2.txt') as f:
        for line in f:
            if check_valid_pass(line):
                total_cnt += 1
            else:
                print('not valid pass')

    print(total_cnt)


if __name__ == '__main__':
    main()



