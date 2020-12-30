import re
from enum import Enum

T = 'top'
R = 'right'
B = 'bottom'
L = 'left'


def get_all_2d_combinations(array):
    """
    Get all possibilities after rotations, flips
    :param array:
    :return: list of 2d arrays.
    """
    all_ps = []
    new_t = array.copy()
    t = Tile(new_t)  # used for all others

    for r in range(4):
        p = t.rotate(r)
        all_ps.append(p)

    for r in range(4):
        p = t.rotate(r)
        p = flip_left_2d_array(p)
        all_ps.append(p)

    for r in range(4):
        p = t.rotate(r)
        p = flip_up_2d_array(p)
        all_ps.append(p)

    for r in range(4):
        d = t.rotate(r)
        d = flip_up_2d_array(d)
        d = flip_left_2d_array(d)
        all_ps.append(d)

    new_ps = all_ps.copy()
    num_ps = len(all_ps)
    for i in range(int(num_ps/2)):
        for j in range(num_ps):
            if i == j:
                continue
            if all_ps[i] == all_ps[j]:
                new_ps.remove(all_ps[j])

    return new_ps


def show_tile(array):
    for i in array:
        if isinstance(i, int):
            i = str(i)
        x = ''.join(i)
        print(x)

    print('show tile ---------------------------------------')


def remove_sides_of_2d_array(array):
    new_a = []
    tmp_list = []
    len_y = len(array)
    len_x = len(array[0])
    for i in range(1, len_y - 1):
        for j in range(len_x):
            tmp_list = array[i][1:-1]
        new_a.append(tmp_list)
    return new_a


def add_right_and_bottom_sides_of_2d_array(array):
    new_a = []
    bottom_list = []
    len_y = len(array)
    len_x = len(array[0])
    for i in range(len_y):
        tmp_list = array[i].copy()
        tmp_list.append(' ')
        new_a.append(tmp_list)

    for j in range(len_x + 1):
        bottom_list.append(' ')

    new_a.append(bottom_list)
    return new_a


def add_right_and_bottom_sides_of_tile_in_pic(array):
    new_a = []
    bottom_list = []
    len_y = len(array)
    len_x = len(array[0])
    for i in range(len_y):
        tmp_list = array[i].copy()
        tmp_list.append(' ')
        new_a.append(tmp_list)

    for j in range(len_x + 1):
        bottom_list.append(' ')

    new_a.append(bottom_list)
    return new_a


def convert_str_to_list(str_in):
    tmp_list = []
    tmp_list[:0] = str_in
    # print(tmp_list)
    return tmp_list


def reverse_list(array):
    return array[::-1]


def rotate_2d_array(original):  # right rotate 90 degree
    l_a = list(zip(*original[::-1]))
    for i in range(len(l_a)):
        l_a[i] = list(l_a[i])

    return l_a


def flip_up_2d_array(original):
    return original[::-1]


def flip_left_2d_array(original):
    tmp_list = []
    for l in original:
        tmp_list.append(l[::-1])
    return tmp_list


class Tile:
    def __init__(self, data):
        self.data = data.copy()  # 2d arrary

    def rotate(self, cnt):
        c = 0
        a = self.data.copy()
        while c < cnt:
            c += 1
            a = rotate_2d_array(a)

        return a

    def get_top(self):
        top = ''
        for d in self.data[0]:
            top += d
        return top

    def get_right(self):
        right = ''
        len_y = len(self.data)
        for i in range(len_y):
            right += self.data[i][-1]
        return right

    def get_bottom(self):
        bottom = ''
        len_y = len(self.data)
        # print(self.data[len_y - 1])
        for d in self.data[len_y - 1]:
            bottom += d
        return bottom

    def get_left(self):
        left = ''
        len_y = len(self.data)
        for i in range(len_y):
            left += self.data[i][0]
        return left

    def get_side(self, side_name):
        if side_name == R:
            return self.get_right()
        elif side_name == L:
            return self.get_left()
        elif side_name == B:
            return self.get_bottom()
        elif side_name == T:
            return self.get_top()


class JigSaw:
    def __init__(self, input):
        self.monster_cnt = 0
        self.d_tiles = dict()  # only edges values different possible values.
        self.d_matchs = dict()
        self.d_no_match = dict()  # {id: [id, id, ...
        self.center_id = ''
        self.ids = set()  # all ids
        self.finish_tiles = set() # finished for matching and rotation
        self.corners = set()
        # for part2:
        self.d_map = dict() # finished new data in tile with id and data after rotation.
        self.d_data = dict()  # raw data for each tile, 2d array, no flip, no rotation at all
        self.map_ids = []  # 2D array, only ids, must be 12 X 12 till touch cornet , it will use d_map to stich later.
        self.pic = []  # whole picture after stich, 2 d array
        self.action_from_corner = 0  # based on left_up corner, all title need to do this extra action. number of rotaion
        with open(input) as f:
            start = True
            for line in f:
                line = line.rstrip()
                m = re.search(r'^Tile (\d+):', line)
                t = re.search(r'[.#]', line)
                if m:
                    id = m.group(1)
                    left = ''
                    right = ''
                    bottom = ''
                    line_cnt = 0
                    two_ds = []  # 2d arrays
                elif t:
                    if line_cnt == 0:
                        top = line
                    elif line_cnt == len(line) - 1:
                        # print('bottom')
                        bottom = line
                    left += line[0]
                    right += line[-1]
                    line_cnt += 1
                    cs = convert_str_to_list(line)
                     two_ds.append(cs)
                    # left = left[::-1]  # keep clock wise
                    # bottom = bottom[::-1] # also keep clock wise
                    # above way will find more than 4 corner ids.
                else:  # must be space:
                    self.d_data[id] = two_ds

                    # total 8 possibilities.
                    self.d_tiles[id] = [top, right, bottom, left, top[::-1], right[::-1], bottom[::-1], left[::-1]]
                    self.ids.add(id)

    # find this tile after any rotation, it has the value passed in ,
    # it can be retrieved from nb's _d_tile value: for very first left up corner. ONLY for this ONE tile.
    # other's use d_map one.get_side , which is the new stardand for other tiles.
    def find_match_tile(self, t_id, d, first_side_name, first_side_value, second_side_name=None,
                        second_side_value=None):
        t_d = Tile(d)
        found = False
        if t_d.get_side(first_side_name) == first_side_value:
            if second_side_name:
                if t_d.get_side(second_side_name) == second_side_value:
                    found = True
            else:
                found = True

        if found:
            self.finish_tiles.add(t_id)
        return found

    def find_matches(self):
        for k, v in self.d_tiles.items():
            tmp_list = []
            tmp_set = set()
            has_match_ids = False
            tmp_no_match = self.ids.copy()
            tmp_no_match.remove(k)
            # print('Start id {}, tmp no match is {}'.format(k, tmp_no_match))
            for kk, vv in self.d_tiles.items():
                if k == kk:
                    continue

                for i in range(4):
                    for j in range(8):
                        if v[i] == vv[j]:
                            # print('Find {} top and {} bottom'.format(k, kk))
                            has_match_ids = True
                            tmp_list.append([i, kk, j])
                            tmp_set.add(kk)
                                                        if kk in tmp_no_match:
                                tmp_no_match.remove(kk)
            if has_match_ids:
                # print('match list len: {}, set {}'.format(len(tmp_list), len(tmp_set)))
                len_set = len(tmp_set)
                if len(tmp_set) == 4:
                    # print('This the the middle one {}'.format(k))
                    # print(tmp_list)
                    self.center_id = k
                elif len_set < 3:
                    # print('This id {} has only {} matches, must be corner tile'.format(k, len_set))
                    self.corners.add(k)

            self.d_matchs[k] = tmp_list
            # print('tmp no match for id {} is {}'.format(k, tmp_no_match))
            self.d_no_match[k] = tmp_no_match

        # print('Find all corners {}'.format(self.corners))

    def m_corners(self):
        m = 1
        for i in self.corners:
            m *= int(i)

        print('Part one: {}'.format(m))

    def find_all_action_with_left_up_corner(self, first_side, second_side):
        set_side = {first_side, second_side}
        if set_side == {0, 3}:
            # print('Need rotation right 180 ')
            self.action_from_corner = 2
        elif set_side == {1, 2}:
            # print('None')
            self.action_from_corner = 0
        elif set_side == {0, 1}:
            # print('Need R90')
            self.action_from_corner = 1
        elif set_side == {2, 3}:
            # print('Need R270')
            self.action_from_corner = 3

    def find_match_sides(self, t_id, first_side_name, first_side_value,
                         second_side_name=None, second_side_value=None):
        new_t = self.d_data[t_id].copy()

        for d in get_all_2d_combinations(new_t):
            if self.find_match_tile(t_id, d, first_side_name, first_side_value, second_side_name, second_side_value):
                return d

        return []

        def start_up_left_corner(self):
        """
        Need to find top left corner id, and then fill up d_maps, using its oritation.
        find action to make it left up.
        Then use get right, down side from Tile class to find who is right and bottom nb
        :return:
        """
        c = self.corners.pop()  # any corner should work

        ns = self.d_matchs[c]
        # print('Corner id {} has nb: {} ----------------------------'.format(c, ns))
        first_nb_id = ns[0][1]
        # find any matches two sides this corner
        self.find_all_action_with_left_up_corner(ns[0][0], ns[1][0])
        # print('Left up tile rotation time: {}'.format(self.action_from_corner))

        new_corner = self.d_data[c].copy()
        # print('Left corner before rotate')
        # show_tile(new_corner)
        for i in range(self.action_from_corner):
            new_corner = rotate_2d_array(new_corner)
            # print('rotate {} time:'.format(i))
            # show_tile(new_corner)
        # print('Left corner after rotate {} times'.format(self.action_from_corner))

        self.d_map[c] = new_corner
        map_id_first_row = [c]  # for map ids

        new_corner_right_value = Tile(new_corner).get_right()  # this is the ONLY value that we need to match nb
        if new_corner_right_value in self.d_tiles[first_nb_id]:  # first id has the value matched.
            right_nb = ns[0]
            bottom_nb = ns[1]
            # print('First nb {} sides has value matches corner right side value, so it is right nb'.format(right_nb[1]))
        else:
            right_nb = ns[1]
            bottom_nb = ns[0]
            # print('First nb {} sides has no value matches corner right side , so it is bottom nb'.format(bottom_nb[1]))

        right_nb_id = right_nb[1]
        right_nb_t = self.find_match_sides(right_nb_id, L, new_corner_right_value)
        if right_nb_t:
            # print('Find right nb {} for left up corner {}'.format(right_nb_id, c))
            # show_tile(right_nb_t)
            self.d_map[right_nb_id] = right_nb_t
            map_id_first_row.append(right_nb_id)
            self.map_ids.append(map_id_first_row)
            # print('map id {} after add first right tile '.format(self.map_ids))
        else:
            print('Find no tile next right to corner tile')
            exit(1)

        # already got bottom
        bottom_nb_id = bottom_nb[1]
        bottom_nb_top_value_from_corner_bottom = Tile(self.d_map[c]).get_bottom()
        # print('Corner {} bottom side value {} will be used for his bottom nb top side'.
        #       format(c, bottom_nb_top_value_from_corner_bottom))

        bottom_nb_t = self.find_match_sides(bottom_nb_id, T, bottom_nb_top_value_from_corner_bottom)
        if bottom_nb_t:
            # print('Find bottom nb {} for left up corner {}'.format(bottom_nb_id, c))
            tmp_new = []
            # show_tile(bottom_nb_t)
            self.d_map[bottom_nb_id] = bottom_nb_t
            tmp_new.append(bottom_nb_id)
            self.map_ids.append(tmp_new)
        else:
            print('Find no tile next down to corner tile with all possibilities')
            exit(1)

        # find how many x , col cnt, go right direction ONLY,
        # use the bottom_nb_id to get the common down one , first row ONLY
        self.stich_right(right_nb_id, 0)
        self.stich_down(bottom_nb_id)  # find how many y, row cnt,

        # go throw each row fro d_map_ids.
        self.stich_right_by_row()

    def stich_pic(self, for_real=True):
        for i in range(len(self.map_ids)):
            tmp_pic_row_all_tiles_dict = dict()  # key is row, value is list
            for j in range(len(self.map_ids[i])):
                tile_data = self.d_map[self.map_ids[i][j]]
                tile_rows_num = len(tile_data)
                for k in range(tile_rows_num):
                    if for_real and (k == 0 or k == tile_rows_num - 1):
                        # first and last row of tile, remove when run real pic, leave it for testing
                        continue
                                        if for_real:
                        stich_row_in_one_tile = tile_data[k][1:-1].copy()  # remove first and last element
                    else:
                        stich_row_in_one_tile = tile_data[k].copy()
                        stich_row_in_one_tile.append(' ')

                    if k not in tmp_pic_row_all_tiles_dict.keys():
                        tmp_pic_row_all_tiles_dict[k] = stich_row_in_one_tile
                    else:
                        tmp_pic_row_all_tiles_dict[k] += stich_row_in_one_tile

            if not for_real:
                for r in range(k + 1):
                    self.pic.append(tmp_pic_row_all_tiles_dict[r])
                self.pic.append([])  # bottom line for each tile.
            else:
                for r in range(1, k):
                    self.pic.append(tmp_pic_row_all_tiles_dict[r])

    def stich_right_by_row(self):
        # print('finish set {}'.format(self.finish_tiles))
        # print('map ids before {}'.format(self.map_ids))
        for i in range(1, len(self.map_ids)):
            # from second row:
            tile_id = self.map_ids[i][0]
            self.stich_right(tile_id, i)

        # print('map ids after stich by row {}'.format(self.map_ids))

    def stich_right(self, right_id, row):
        """
                find how many tiles to the right direction, called recursively, till touch the corner or none, edge
        :param right_id:  small tile id, and row is d_map id, which will be used for pic row id.
        :return:
        """
        # print('add map id to right from tile {} on row {}'.format(right_id, row))
        ns = self.d_matchs[right_id]
        # print('Right nb id {} has nb: {} ----------------------------'.format(right_id, ns))
        for n in ns:
            right_nb_id = n[1]

            if right_nb_id in self.finish_tiles or right_nb_id in self.d_map.keys():  # must be his left nb, ignore
                continue

            right_nb_left_value = Tile(self.d_map[right_id]).get_right()

            # print('Tile {} right side value {} will be used for his right nb left side'.format(right_id,
            #                                                                                    right_nb_left_value))
            if right_nb_left_value not in self.d_tiles[right_nb_id]:
                # print('{} is not right nb of {} since not find any side value in his posibilites list'.format(right_nb_id, right_id))
                continue

            right_nb_t = self.find_match_sides(right_nb_id, L, right_nb_left_value)
            if right_nb_t:
                # pic_row = row * len(right_nb_t)
                # self.stich_pic_right(pic_row, right_nb_t)
                # print('Find right nb id {} of {} !!!!!!!!!!!!!!!!!!!'.format(right_nb_id, right_id))
                self.d_map[right_nb_id] = right_nb_t
                # # show_tile(right_nb_t)
                self.map_ids[row].append(right_nb_id)
                if right_nb_id not in self.corners:
                    self.stich_right(right_nb_id, row)  # go further, util end
            else:
                print('Right nb of id {} is not found!!!!!'.format(right_id))
                exit(1)

    def find_monster(self):
        hd_str = '..................#.'
        bd_str = '#....##....##....###'
        lg_str = '.#..#..#..#..#..#...'
        
                m_ps = 0
        m_ps += len(re.findall('#', bd_str + lg_str)) + 1
        # print('Monster has {} #s'.format(m_ps))
        for a in get_all_2d_combinations(self.pic):
            all_ps = 0
            for r in range(len(a)):
                # print('row line {} '.format(r))
                row = ''.join(a[r])
                all_ps += len(re.findall('#', row))
                for b in re.finditer(r'#....##....##....###', row):
                    self.check_monster_by_body_one_by_one(a, r, b.span())

        print('Total monster count {}'.format(self.monster_cnt))
        print('All ps {}'.format(all_ps))
        m_ps_all = m_ps * self.monster_cnt
        print('Total ps on monster {}'.format(m_ps_all))
        print('Total wave {}'.format(all_ps - m_ps_all))

    def check_monster_by_body_one_by_one(self, a, r, body_span):
        leg_row = ''.join(a[r + 1])
        leg_str = leg_row[body_span[0]:body_span[1]]
        head_row = ''.join(a[r - 1])
        head_str = head_row[body_span[0]:body_span[1]]

        if re.search(r'.#..#..#..#..#..#...', leg_str) and re.search(r'..................#.', head_str):
            self.monster_cnt += 1

    def stich_down(self, bottom_id):
        """
        ONLY use for first column, edge down. to get row cnt, y cnt.  And start id for each row,
        :param bottom_id:
        :return:
        """
        ns = self.d_matchs[bottom_id]
        # print('One of the right or down nb id {} has nb: {} ----------------------------'.format(bottom_id, ns))
        for n in ns:
            # print('n {}'.format(n))
            bottom_nb_id = n[1]
            bottom_nb_top_value_ind = n[2]
            if bottom_nb_id in self.finish_tiles or bottom_nb_id in self.d_map.keys():  # must be his up nb, ignore
                continue

            bottom_nb_top_value = Tile(self.d_map[bottom_id]).get_bottom()

            # print('Tile {} bottom side value {} will be used for his bottom nb top side'.format(bottom_id,
            #        
                        if bottom_nb_top_value not in self.d_tiles[bottom_nb_id]:
                # print('{} sides have no value matches its top nb {}'.format(bottom_nb_id, bottom_id))
                continue

            bottom_nb_t = self.find_match_sides(bottom_nb_id, T, bottom_nb_top_value)
            if bottom_nb_t:
                tmp_row = []
                self.d_map[bottom_nb_id] = bottom_nb_t
                # show_tile(bottom_nb_t)
                tmp_row.append(bottom_nb_id)
                self.map_ids.append(tmp_row)
                if bottom_nb_id not in self.corners:
                    self.stich_down(bottom_nb_id)
            else:
                print('Bottom nb of id {} is not found!!!!!'.format(bottom_id))
                exit(1)

# example:
# js = JigSaw('d20.txt')
# js.find_matches()
# print('Center : {}'.format(js.center_id))
# js.find_corners()


# part one:
js = JigSaw('day20.txt')
js.find_matches()
js.m_corners()

print('Start part two')
js.start_up_left_corner()

# for testing stich
# js.stich_pic(for_real=False)
# print('Show the pic: {}==========================')
# show_tile(js.pic)
# print('Done sow the pic: {}==========================')

# find monster - part2:
js.stich_pic()
js.find_monster()



             
