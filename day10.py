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
    p_cnt = 1
    list_nums = []
    list_nums.append(tuple(nums))
    i = 0 
    while i < (len(nums) - 1):  # nums has most len, so it is fine here
        print('i is {}'.format(i))
        print('New len of list_nums {}'.format(len(list_nums)))
        for t in list_nums:
            n = list(t) 
#            print('Dealing with n: {}'.format(n))
            if (i + 2) < len(n) and (n[i+2] - n[i]) < 4:
                tmp_nums = n.copy()
                tmp_nums.remove(n[i+1])
                print('Adding {}'.format(tmp_nums))
                list_nums.append(tuple(tmp_nums))
                p_cnt += 1

            if (i + 3) < len(n) and (n[i+3] - n[i]) < 4:
                tmp_nums = n.copy()
                tmp_nums.remove(n[i+1])
                tmp_nums.remove(n[i+2])
                list_nums.append(tuple(tmp_nums))
                print('Adding2 {}'.format(tmp_nums))
                p_cnt += 1

        i += 1

    print('Part2: {}'.format(list_nums))
    print('Part2: {}'.format(len(set(list_nums))))



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
    nums = get_nums_from_file('d10.txt')
    # nums = get_nums_from_file('da10.txt')
    # nums = get_nums_from_file('day10.txt')

    part1(nums)
    part2(nums)

if __name__ == '__main__':
    main()
