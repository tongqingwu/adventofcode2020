import re

EAST = 'east'
WEST = 'west'
NORTH = 'north'
SOUTH = 'south'

def main():
    x = 0
    y = 0
    w_x = 10
    w_y = 1
    with open('day12.txt') as f:
    # with open('d12.txt') as f:
        for line in f:
            line = line.rstrip()
            d = re.search(r'(\S)(\d+)', line)
            if d:
                action = d.group(1) 
                nm = int(d.group(2))
                print(line)
                direction = get_current_direction(w_x, w_y)
                print('Direction: {}, x {}, y {}, w_x {}, w_y {}'.format(direction, x, y, w_x, w_y))
                if action == 'F':
                    print('w_x {}, w_y {}'.format(w_x, w_y))
                    x += nm * w_x
                    y += nm * w_y
                    print('x {}, y {}'.format(x, y))
                elif action == 'N':
                    w_y += nm
                elif action == 'E':
                    w_x += nm
                elif action == 'W':
                    w_x -= nm
                elif action == 'S':
                    w_y -= nm
                elif (action == 'R' and nm == 90) or (action == 'L' and nm == 270):
                    if direction == EAST:
                        w_x, w_y = turn_to_south(w_x, w_y)
                        print('Turn south w_x {}, w_y {}'.format(w_x, w_y))
                    elif direction == SOUTH:
                        w_x, w_y = turn_to_west(w_x, w_y)
                    elif direction == WEST:
                        w_x, w_y = turn_to_north(w_x, w_y)
                    elif direction == NORTH:
                        w_x, w_y = turn_to_east(w_x, w_y)
                elif (action == 'R' and nm == 180) or (action == 'L' and nm == 180):
                    print('180 degree, w_x {}, w_y {}'.format(w_x, w_y))
                    w_x = (-1) * w_x
                    w_y = (-1) * w_y
                    print('After turn 180 degree, w_x {}, w_y {}'.format(w_x, w_y))
                elif (action == 'R' and nm == 270) or (action == 'L' and nm == 90):
                    if direction == EAST:
                        w_x, w_y = turn_to_north(w_x, w_y)
                    elif direction == SOUTH:
                        w_x, w_y = turn_to_east(w_x, w_y)
                    elif direction == WEST:
                        w_x, w_y = turn_to_south(w_x, w_y)
                    elif direction == NORTH:
                        w_x, w_y = turn_to_west(w_x, w_y)

    print('x is {}'.format(x))
    print('y is {}'.format(y))
    distance = abs(x) + abs(y)
    print('Part one: {}'.format(distance))


def get_current_direction(w_x, w_y):
    if w_x > 0 and w_y > 0:
        return EAST
    elif w_x > 0 and w_y < 0:
        return SOUTH 
    elif w_x < 0 and w_y < 0:
        return WEST 
    elif w_x < 0 and w_y > 0:
        return NORTH 


def turn_to_east(x, y):
    w_x = abs(y)
    w_y = abs(x)
    return w_x, w_y


def turn_to_north(x, y):
    w_x = 0 - abs(y)
    w_y = abs(x)
    return w_x, w_y


def turn_to_south(x, y):
    print('turn south w_x {}, w_y {}'.format(x, y))
    w_x = abs(y)
    w_y = 0 - abs(x)
    print('After turn south w_x {}, w_y {}'.format(w_x, w_y))
    return w_x, w_y


def turn_to_west(x, y):
    w_x = 0 - abs(y)
    w_y = 0 - abs(x)
    return w_x, w_y


if __name__ == '__main__':
    main()

