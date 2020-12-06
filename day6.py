import re

def get_group_yes_count(yes_str):
    # print('yes str, combine all in group: {}'.format(yes_str))
    set_yes = set(yes_str)
    # print(set_yes)
    return len(set_yes)


def find_common_elements(list_of_set):
    if len(list_of_set) == 0:
        return 0
    # print('Group ------------- {}'.format(list_of_set))
    commons = list_of_set[0]
    list_of_set.remove(list_of_set[0])
    while len(list_of_set) > 0:
        # print('in while: commons {}, firt set {}'.format(commons, list_of_set[0]))
        commons = get_common_elements(commons, list_of_set[0])
        list_of_set.remove(list_of_set[0])

    cnt = len(commons)
    # print('common in this group {}, cnt {}'.format(commons, cnt))
    return len(commons)


def get_common_elements(set1, set2):
    return set1 & set2


def main():


    cnt = 0
    cnt_common = 0

    with open('day6.txt') as f:
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

