import re


FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def check_hcl(hcl):
    if len(hcl) != 7:
        print('hcl wrong length')
        return False

    if not re.search(r'^#[a-f0-9]+$', hcl):
        print('hcl wrong')
        return False

    return True


def check_hgt(hgt):
    if 'cm' in hgt:
        h_cm = int(hgt.replace('cm', ''))
        if h_cm < 150 or h_cm > 193:
            print('cm out of range')
            return False
    elif 'in' in hgt:
        h_in = int(hgt.replace('in', ''))
        if h_in < 59 or h_in > 76:
            print('in out of range')
            return False
    else:
        print('No cm or in')
        return False

    return True


def check_valid_pass(i_dict):
    is_valid = True
    for f in FIELDS:
        if f not in i_dict:
            print('{} not in dict'.format(f))
            return False

        # part 2
    if not check_hgt(i_dict['hgt']):
        print('hgt is wrong')
        return False

    byr = int(i_dict['byr'])
    if byr < 1920 or byr > 2002:
        print('byr is wrong')
        return False

    iyr = int(i_dict['iyr'])
    if iyr < 2010 or iyr > 2020:
        print('iyr is wrong')
        return False

    eyr = int(i_dict['eyr'])
    if eyr < 2020 or eyr > 2030:
        print('eyr is wrong')
        return False

    if i_dict['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        print('ecl is wrong')
        return False

    if not check_hcl(i_dict['hcl']):
        print('hcl is wrong')
        return False

    if not re.search(r'^\d\d\d\d\d\d\d\d\d$', i_dict['pid']):
        print('pid is wrong')
        return False

    return is_valid


def main():
    cnt = 0
    total_p = 0

    with open('day4.txt') as f:
        id_dict = {}
        for line in f:
            line = line.rstrip()
            d = re.search(r'(\S):(\S+)', line)
            if d:
                pairs = line.split(' ')
                for p in pairs:
                    (k, v) = p.split(':')
                    id_dict[k] = v
            else:
                print(id_dict)
                if check_valid_pass(id_dict):
                    cnt = cnt + 1
                    print('valid id')
                else:
                    print('Invalid id')

                id_dict = {}

    print(cnt)


if __name__ == '__main__':
    main()  # part one 228.
