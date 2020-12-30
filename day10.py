cnt_one = 0
cnt_three = 0


def get_nums_from_file(f_name):
    nums = []
    with open(f_name) as f:
        for line in f:
            line = line.rstrip()
            nums.append(int(line))
    nums.sort()
    # print(nums)
    return nums


def part2(nums):
    # print(find_p_no_recursive(4))
    p = 1
    l_slices = get_slices(nums)
    # print(l_slices)
    for s in l_slices:
        p *= find_p_no_recursive(len(s))

    print('Part2: {}'.format(p))


def get_one_and_three_jolts(nums):
    cnt_diffs(0, nums[0])
    i = 0 
    while i < (len(nums) - 1): 
        cnt_diffs(nums[i], nums[i+1])
        i += 1


def cnt_diffs(j_one, j_two):
    global cnt_one
    global cnt_three
    diff_j = j_two - j_one 

    if diff_j == 1:
        cnt_one += 1
    elif diff_j == 3:
        cnt_three += 1


def part1(nums):
    get_one_and_three_jolts(nums)
    # print('cnt one {}'.format(cnt_one))
    # last 3 add one more:
    # print('cnt three {}'.format(cnt_three + 1))
    print('Part 1: {}'.format(cnt_one * (cnt_three + 1)))


def get_slices(nums):
    # print(len(nums))
    l_slices = []
    tmp_s = []
    for i in range(len(nums)):
        if i == 0:
            tmp_s.append(nums[0])
        else:
            if nums[i] - nums[i - 1] == 3:
                l_slices.append(tmp_s)
                tmp_s = []

            tmp_s.append(nums[i])

    l_slices.append(tmp_s)
    return l_slices


# slow
def find_p(n):
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
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n == 3:
        return 2
    elif n == 4:
        return 4

    p_list = [1,1,2,4]
    while n != len(p_list):
        p_list.append(p_list[-1]+p_list[-2]+p_list[-3])
    # print(p_list)

    return p_list[-1]


def main():
    # nums = get_nums_from_file('da10.txt')
    # nums = get_nums_from_file('da10.txt')
    nums = get_nums_fro
