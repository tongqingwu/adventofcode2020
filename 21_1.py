import re

def part1():
    h = 0
    d = 0

    with open('21_1.txt') as f:
        id_dict = {}
        for line in f:
            line = line.rstrip()
            t = re.search(r'(\S+) (\d+)', line)
            if t:
                direct = t.group(1)
                val = int(t.group(2))
       #         print(val)
                if direct == 'forward':
                    h += val
                elif direct == 'up':
                    d = d - val
                elif direct == 'down':
                    d += val
    res = h * d
    print(res)


def part2():
    h = 0
    d = 0
    a = 0

    with open('21_1.txt') as f:
    #with open('21_1_0.txt') as f:
        id_dict = {}
        for line in f:
            line = line.rstrip()
            t = re.search(r'(\S+) (\d+)', line)
            if t:
                direct = t.group(1)
                val = int(t.group(2))
       #         print(val)
                if direct == 'forward':
                    h += val
                    d += a * val
                elif direct == 'up':
                    a = a - val
                elif direct == 'down':
                    a += val
    res = h * d
    print(res)


if __name__ == '__main__':
    part1()  
    part2() 
