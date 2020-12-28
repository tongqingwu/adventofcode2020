import re

d_action = {'e': (1, -1, 0),
            'w': (-1, 1, 0),
            'ne': (0, -1, 1),
            'nw': (-1, 0, 1),
            'se': (1, 0, -1),
            'sw': (0, 1, -1)}


def get_tile_id_by_prev(prev, act):
    current = []
    for i in range(len(prev)):
        current.append(list(prev)[i] + d_action[act][i])
    return tuple(current)


class HexTile:
    def __init__(self, input_file):
        self.tiles = dict()  # {(3, -2, 1): flip cnt/color  (  0,2,4 - white, 1,3, 5 - black etc.)}
        self.black_tiles = dict()  # only for black tile
        self.tiles_new = dict() # part 2 next day, all black ones plus the ones in his 6 nb.  # ex. 10 black, 60 nb.
        self.white_tiles = dict()  # only for part 2, all white tiles around black tiles, will be merged to tiles new with black tiles
        self.total_black = 0
        self.day_cnt = 0

        self.cnt = 0
        with open(input_file) as f:

            for line in f:
                self.cnt += 1
                line = line.rstrip()
                pattern = re.compile(r'nw|sw|ne|se|w|e')
                l_a = pattern.findall(line)
                self.find_flip_tile(l_a)

    def find_flip_tile(self, l_a):
        print(l_a)
        prev = (0, 0, 0)
        for a in l_a:
            c_t = get_tile_id_by_prev(prev, a)
            # print('Prev {}, move {} to current {}'.format(prev, a, c_t))

            prev = c_t
        self.update_dict(c_t)

    def update_dict(self, c_t):
        if c_t in self.tiles.keys():
            print('Visit {} before'.format(c_t))
            self.tiles[c_t] += 1
        else:
            self.tiles[c_t] = 1

        def part2(self, day_cnt):
        for i in range(day_cnt):
            print('Before checking in day {} has {} black'.format(self.day_cnt, len(self.black_tiles)))
            self.tiles_new = self.black_tiles.copy()
            d_tile_new = dict()
            self.white_tiles = dict()
            for k, v in self.black_tiles.items():
                # print('Checking black tiles nbs')

                cnt_black = self.cnt_nb_of_black(k)
                if cnt_black == 0 or cnt_black > 2:
                    self.tiles_new[k] += 1

            # has white tiles from above action
            for k, v in self.white_tiles.items():
                # print('Checking white tiles nbs')
                cnt_black = self.cnt_nb_of_white(k)
                if cnt_black == 2:
                    self.tiles_new[k] = 1  # add a black to tile_new

            self.cnt_flips(check_new_tiles=True)

    def cnt_nb_of_white(self, prev):
        """
        Check nbs of white
        :param prev:
        :return:
        """
        total_black = 0
        for k, v in d_action.items():
            t = get_tile_id_by_prev(prev, k)
            if t in self.black_tiles.keys():
                total_black += 1

        return total_black

    def cnt_nb_of_black(self, prev):
        """
        Check nbs of black, also update self.tiles_new with white tile around those black's.
        :param prev:
        :return:
        """
        total_black = 0
        for k, v in d_action.items():
            t = get_tile_id_by_prev(prev, k)
            if t in self.black_tiles.keys():
                total_black += 1
            else:
                self.white_tiles[t] = 0
        return total_black

    def cnt_flips(self, check_new_tiles=False):
        """
        New tiles is after check nb's.
        :param check_new_tiles:
        :return:
        """
        d_black = dict()
        if check_new_tiles:
            d_t = self.tiles_new.copy()
        else:
            d_t = self.tiles.copy()   # only used for before day1,
        for k, v in d_t.items():
            # print('k {}, v {}'.format(k, v))
            if v == 0:
                print('v 0 white')
            else:
                if v % 2 != 0:
                    d_black[k] = v
                    self.black_tiles = d_black # will be used for day one, day two, etc.

        print('Total black {} on day {}'.format(len(self.black_tiles), self.day_cnt))
        self.day_cnt += 1


ht = HexTile('day24.txt')
print('Cnt of before day 1, all flip tiles, including white which flip more than once:')
ht.cnt_flips()
print('start check from day one now -------------- part 2:')
ht.part2(100)
