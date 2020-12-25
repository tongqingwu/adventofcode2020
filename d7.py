import re


def get_common_elements(set1, set2):
    return set1 & set2


def main():


    cnt = 0
    cnt_common = 0

    with open('day7.txt') as f:
        yes_str = ''
        group = [] # list of set
        for line in f:
            line = line.rstrip()
            d = re.search(r'(\S+)', line)
            if d:
                yes_str += line
                group.append(set(line))
            else:
                # print(yes_str)
                cnt_common += find_common_elements(group)
                cnt += get_group_yes_count(yes_str)

                yes_str = ''  # reset yes_str for next group
                group = []

    print(cnt)
    print(cnt_common)


if __name__ == '__main__':
    main()

