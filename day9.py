def get_nums_from_file(f_name):
    nums = []
    with open(f_name) as f:
        for line in f:
            line = line.rstrip()
            nums.append(int(line))
    return nums


def find_bad_sum(nums):
    last_num = nums.pop()
    if last_num not in get_sum_set_from_nums(nums):
        return last_num
    else:
        return 0


def get_sum_set_from_nums(nums):
    s_set = set()
    for i in nums:
        for j in nums:
            if i != j:
                s_set.add(i + j)
    return s_set


def get_part1_end(nums, preamble_cnt):
    slice_cnt = preamble_cnt + 1

    start = 0
    end = 0
    while end < len(nums):
        end = start + slice_cnt
        tmp_list = nums[start:end]
        bad = find_bad_sum(tmp_list)
        if bad != 0:
            print('Part One answer : {}'.format(bad))
            return end

        start = start + 1


def find_sum_match(nums, cnt, sum_num):
    start = 0
    end = 0
    while end < len(nums):
        end = start + cnt
        tmp_list = nums[start:end]
        if sum(tmp_list) == sum_num:
            print('Part Two answer: {}'.format(find_sum_of_smallest_largest(tmp_list)))
            return True

        start = start + 1

    return False


def find_sum_of_smallest_largest(nums):
    nums.sort()
    return nums.pop(0) + nums.pop()


def main():
    nums = get_nums_from_file('d9.txt')
    end = get_part1_end(nums, 5)

    # nums = get_nums_from_file('day9.txt')
    # end = get_part1_end(nums, 25)

    part1_num = nums[end - 1]
    new_nums = nums[0:end - 1]

    cnt = 2
    while not find_sum_match(new_nums, cnt, part1_num) and cnt < part1_num:
        cnt += 1


if __name__ == '__main__':
    main()
