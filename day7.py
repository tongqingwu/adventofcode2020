import re

all_bags = 0


def find_parents_from_bag_names(names):
    parents = set()
    with open('day7.txt') as f:
        for line in f:
            line = line.rstrip()
            d = re.search(r'(.+) bags contain (.+)', line)
            if d:
                if any(x in d.group(2) for x in names):
                    parents.add(d.group(1))

    return parents


def find_children_from_bag_name(name, cnt):
    global all_bags
    all_bags += cnt  # only this bag count
    with open('day7.txt') as f:
        for line in f:
            line = line.rstrip()
            d = re.search(r'^' + name + ' bags contain (\d.+)', line)
            if d:
                dict_children = get_bag_dict(d.group(1))
                for k, v in dict_children.items():
                    find_children_from_bag_name(k, cnt * v)


def get_bag_dict(string):
    bag_dict = dict()
    for b in string.split(', '):
        d = re.search(r'(\d+) (.+) bag', b)
        if d:
            bag_dict[d.group(2)] = int(d.group(1))

    return bag_dict


def part1():
    bags = set()

    p = find_parents_from_bag_names({'shiny gold'})
    bags = bags.union(p)
    while len(p) > 0:
        p = find_parents_from_bag_names(p)
        bags = bags.union(p)

    print(len(bags))


def main():
    part1()
    find_children_from_bag_name('shiny gold', 1)
    print(all_bags - 1)


if __name__ == '__main__':
    main()

