cnt_one = 0
cnt_three = 0

def get_nums_from_file(f_name):
    nums = []
    with open(f_name) as f:
        for line in f:
            line = line.rstrip()
            nums.append(int(line))
    nums.sort()
    print(nums)
    return nums


def part2(nums):

    print('Part2: {}'.format(list_nums))
    print('Part2: {}'.format(len(set(list_nums))))


# slow 
def def find_p(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n == 3:
        return 2
    else:
        return find_p(n - 1) + find_p(n - 2) + find_p(n - 3)


# quick
def find_p_no_recursive(n):
    list1 = [1,1,2,4]
    while (n != len(list1)):
        list1.append(list1[-1]+list1[-2]+list1[-3])
    print(list1)

    return list1[-1]


def get_one_and_three_jolts(nums):
    cnt_diffs(0, nums[0])
    i = 0 
    while i < (len(nums) - 1): 
        #print('i is {}'.format(i))
        #print('num now {}'.format(nums[i]))
        #print('num next now {}'.format(nums[i + 1]))
        cnt_diffs(nums[i], nums[i+1])
        i += 1


def cnt_diffs(j_one, j_two):
    global cnt_one
    global cnt_three
    # print('j2 {}'.format(j_two))
    # print('j1 {}'.format(j_one))
    diff_j = j_two - j_one 

    if diff_j == 1:
       cnt_one += 1
    elif diff_j == 3:
       cnt_three += 1 


def part1(nums):
    get_one_and_three_jolts(nums)
    print('cnt one {}'.format(cnt_one))
    # last 3 add one more:
    print('cnt three {}'.format(cnt_three + 1))
    print('Part 1: {}'.format(cnt_one * (cnt_three + 1)))


def main():
    # nums = get_nums_from_file('d10.txt')
    nums = get_nums_from_file('da10.txt')
    # nums = get_nums_from_file('day10.txt')
    nums.insert(0, 0)
    part1(nums)
    part2(nums)


if __name__ == '__main__':
    main()
