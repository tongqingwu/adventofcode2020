def find_2020(nums):
    while len(nums) > 2:
        # print(nums)
        num = nums[0]
        # print(num)
        nums.pop(0)
        # print(nums)
        for i in nums:
            # print(i)
            sum = i + num
            if sum == 2020:
                print('Found {} and {}'.format(num, i))
                print(i * num)
                nums.remove(i)


def find_2020_part2(nums):
    m = 0
    while len(nums) > 3:
        num = nums[0]
        # print('num {}'.format(num))

        # if num < 694:
        #     print('num {} is small'.format(num))

        nums.pop(0)
        nums_tmp = nums.copy()
        for i in nums:
            num2 = num + i
            if num2 > 2020:
                continue
            # print('num2 {}'.format(num2))
            nums_tmp.remove(i)

            # print('nums {}'.format(nums))
            # print('n_tm {}'.format(nums_tmp))
            for j in nums_tmp:
                sum = j + num2
                if sum == 2020:
                    # print('-----------------Found {}, {} and {}'.format(num, i, j))
                    m = i * j * num
                    nums.remove(i)
                    nums.remove(j)
        # print('nums len {}'.format(len(nums)))
    return m


def main():
    numbers = []

    with open('day1.txt') as f:
        for line in f:
            numbers.append(int(line.rstrip()))

    # find_2020(numbers)  # 357504
    m = find_2020_part2(numbers)
    print(m)

if __name__ == '__main__':
    main()
