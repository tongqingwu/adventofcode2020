import re

EAST = 'east'
WEST = 'west'
NORTH = 'north'
SOUTH = 'south'

def main():
    x = 0
    y = 0
    with open('day12.txt') as f:
    # with open('d12.txt') as f:
        direction = EAST 
        for line in f:
            line = line.rstrip()
            d = re.search(r'(\S)(\d+)', line)
            if d:
                action = d.group(1) 
                nm = int(d.group(2))
                print('Direction {}, action {}, nm {}'.format(direction, action, nm))
                if action == 'F':
                    print('ACT F')
                    if direction == EAST:
                        x += nm
                        print('East nm {}, x {}'.format(nm, x))
                    elif direction == WEST:
                        x -= nm
                    elif direction == NORTH:
                        y += nm
                    elif direction == SOUTH:
                        y -= nm
                elif action == 'N':
                    y += nm
                elif action == 'E':
                    x += nm
                elif action == 'W':
                    x -= nm
                elif action == 'S':
                    y -= nm
                elif action == 'R':
                    print('Turn R')
                    if direction == WEST:
                        if nm == 90:
                            direction = NORTH
                        elif nm == 180:
                            direction = EAST 
                        elif nm == 270:
                            direction = SOUTH 
                    elif direction == EAST:
                        if nm == 90:
                            print('Turn South')
                            direction = SOUTH
                        elif nm == 180:
                            direction = WEST 
                        elif nm == 270:
                            direction = NORTH 
                    elif direction == SOUTH:
                        if nm == 90:
                            direction = WEST 
                        elif nm == 180:
                            direction = NORTH 
                        elif nm == 270:
                            direction = EAST 
                    elif direction == NORTH:
                        if nm == 90:
                            direction = EAST 
                        elif nm == 180:
                            direction = SOUTH 
                        elif nm == 270:
                            direction = WEST 
                elif action == 'L':
                    if direction == WEST:
                        if nm == 90:
                            direction = SOUTH 
                        elif nm == 180:
                            direction = EAST
                        elif nm == 270:
                            direction = NORTH
                    elif direction == EAST:
                        if nm == 90:
                            direction = NORTH
                        elif nm == 180:
                            direction = WEST
                        elif nm == 270:
                            direction = SOUTH
                    elif direction == SOUTH:
                        if nm == 90:
                            direction = EAST
                        elif nm == 180:
                            direction = NORTH
                        elif nm == 270:
                            direction = WEST 
                    elif direction == NORTH:
                        if nm == 90:
                            direction = WEST 
                        elif nm == 180:
                            direction = SOUTH
                        elif nm == 270:
                            direction = EAST

    print('x is {}'.format(x))
    print('y is {}'.format(y))
    if x < 0:
        x = 0 - x
    if y < 0:
        y = 0 - y
    distance = x + y
    print('Part one: {}'.format(distance))


if __name__ == '__main__':
    main()

