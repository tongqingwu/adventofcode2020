import sys
import numpy as np

def get_str(str):
    ans = ""
    for char in str:
        if char == "#":
            ans += "1"
        if char == ".":
            ans += "0"

    return ans

def str_flip(str):
    flip_str = str[::-1]
    return flip_str

# -----------------------------------------------------

def convert_list_to_counts(lis):
    counts = dict()
    for num in lis:
        counts[num] = counts.get(num, 0) + 1

    return counts

def which_tiles(dic, cond):
    ans = []
    for key in dic:
        if dic[key] == cond:
            ans += [key]

    return ans

# -----------------------------------------------------

def get_neighbor(current_tile_num, the_side, reverse):
    possibilities = reverse[the_side]

    if len(possibilities) == 1:
        return None

    else:
        if possibilities[0] != current_tile_num:
            return possibilities[0]
        return possibilities[1]

def convert_to_txt(final_build):
    tile_size = len(final_build[0][0].interior)
    num_tiles = len(final_build[0])

    puzzle = ""

    for vertical in range(num_tiles):
        for sub_height in range(tile_size):
            for lateral in range(num_tiles):
                puzzle +="".join(final_build[vertical][lateral].interior[sub_height])
            puzzle += "\n"
        # puzzle += "\n\n"

    return puzzle

# -----------------------------------------------------

def convert_txt_to_numpy(puzzle):
    puzzle = puzzle.split("\n")
    ans = np.empty((len(puzzle)-1, len(puzzle[0])), dtype=str)

    for i in range(len(puzzle)-1):
        ans[i] = np.array(list(puzzle[i]))

    return ans

def count_sea_monsters(puzzle):

    sea_monsters = 0
    hash_tags = 0

    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] == '#':
                hash_tags += 1

    for v in range(1, len(puzzle) - 1):
        for h in range(len(puzzle[0])-19):
            if puzzle[v][h] == '#' and puzzle[v][h+5] == '#' and puzzle[v][h+6] == '#' and puzzle[v][h+11] == '#' and puzzle[v][h+12] == '#' and puzzle[v][h+17] == '#' and puzzle[v][h+18] == '#' and puzzle[v][h+19] == '#':
                if puzzle[v-1][h+18] == '#':
                    if puzzle[v+1][h+1] == '#' and puzzle[v+1][h+4] == '#' and puzzle[v+1][h+7] == '#' and puzzle[v+1][h+10] == '#' and puzzle[v+1][h+13] == '#' and puzzle[v+1][h+16] == '#':
                        sea_monsters += 1

    # print(sea_monsters, (hash_tags - (sea_monsters * 15)))
    return sea_monsters, (hash_tags - (sea_monsters * 15))

    # .#.#...#.###...#.##.O#..
    # O.##.OO#.#.OO.##.OOO
    # ..#O.#O#.O##O..O.#O##.##


# -----------------------------------------------------

class Tile:
    def __init__(self, id, north, east, south, west, interior):
        self.id = id
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.interior = interior

    def print(self):
        print("Tile number: {}".format(self.id))
        print(self.north)
        print(self.east)
        print(self.south)
        print(self.west)
        print(self.interior)

    def rotate_times(self, num):
        for i in range(num):
            self.rotate()

    def rotate(self):   # clockwise rotation
        new_north = self.west
        new_east = self.north
        new_south = self.east
        new_west = self.south

        self.north = new_north
        self.east = new_east
        self.south = new_south
        self.west = new_west

        self.interior = np.rot90(self.interior, 3)

    def flip(self): # flip from side to side
        new_north = str_flip(self.north)
        new_south = str_flip(self.south)
        new_west = str_flip(self.east)
        new_east = str_flip(self.west)

        self.north = new_north
        self.east = new_east
        self.south = new_south
        self.west = new_west

        self.interior = np.fliplr(self.interior)

    # tile.get_side_to("#.#####...#", top)
    def get_side_to(self, the_side, direction):
        if direction == "north" and self.north == the_side:
            return
        elif direction == "east" and self.east == the_side:
            return
        elif direction == "south" and self.south == the_side:
            return
        elif direction == "west" and self.west == the_side:
            return

        elif the_side not in [self.north, self.east, self.south, self.west]:
            self.flip()
            return self.get_side_to(the_side, direction)

        else:
            self.rotate()
            return self.get_side_to(the_side, direction)

    def delete_border(self):
        self.interior = np.delete(self.interior, 0, 0)
        self.interior = np.delete(self.interior, -1, 0)
        self.interior = np.delete(self.interior, 0, 1)
        self.interior = np.delete(self.interior, -1, 1)


def solution(filename):
    f = open("./inputs/" + filename, 'r')
    f = f.read().split("\n\n")

    actual_tiles = dict()  # key: id, value: the Tile() that has that id
    tiles = dict()  # key: id, value: north, east, south, west, f_north, f_east, f_south, f_west
    counts = dict() # key: side_num, value: number of occurrences counted
    reverse = dict()    # key: side_num, value: the tile where it could have came from

    for tile in f:
        tile_number = int(tile.split("\n")[0].split(" ")[1][:-1])
        tile_rows = tile.split("\n")[1:]

        north = get_str(tile_rows[0])
        south = get_str(tile_rows[-1][::-1])
        west = get_str(("".join([x[0] for x in tile_rows]))[::-1])
        east = get_str("".join([x[-1] for x in tile_rows]))

        interior = np.empty((len(tile_rows), len(tile_rows)), dtype=str)
        for i in range(len(tile_rows)):
            for j in range(len(tile_rows)):
                interior[i][j] = tile_rows[i][j]

        the_tile = Tile(tile_number, north, east, south, west, interior)

        # ----------------------------------
        # dictionary loading below     v

        actual_tiles[tile_number] = the_tile
        tiles[tile_number] = [north, east, south, west, str_flip(north), str_flip(east), str_flip(south), str_flip(west)]

        for side in [north, east, south, west, str_flip(north), str_flip(east), str_flip(south), str_flip(west)]:
            reverse[side] = reverse.get(side, []) + [tile_number]
            counts[side] = counts.get(side, 0) + 1

    # loading information above ^
    # -------------------------------------

    tiles_counts = dict()
    for key in tiles:
        tiles_counts[key] = convert_list_to_counts(list(map(lambda x: counts[x], tiles[key])))

    corners = which_tiles(tiles_counts, {1: 4, 2: 4})

    standard_corner = corners[0]

    if counts[actual_tiles[standard_corner].north] == 2 and counts[actual_tiles[standard_corner].east] == 2:
        actual_tiles[standard_corner].rotate()

    elif counts[actual_tiles[standard_corner].east] == 2 and counts[actual_tiles[standard_corner].south] == 2:
        pass

    elif counts[actual_tiles[standard_corner].south] == 2 and counts[actual_tiles[standard_corner].west] == 2:
        actual_tiles[standard_corner].rotate_times(3)

    elif counts[actual_tiles[standard_corner].west] == 2 and counts[actual_tiles[standard_corner].north] == 2:
        actual_tiles[standard_corner].rotate_times(2)


    final_build = dict()
    final_build[0] = dict()
    final_build[0][0] = actual_tiles[standard_corner]

    # final_build[0][0].print()

    ind = 0
    while get_neighbor(final_build[0][ind].id, final_build[0][ind].east, reverse) is not None:
        adj_tile = actual_tiles[get_neighbor(final_build[0][ind].id, final_build[0][ind].east, reverse)]

        ind += 1
        final_build[0][ind] = adj_tile
        final_build[0][ind].get_side_to(str_flip(final_build[0][ind-1].east), "west")
        # final_build[0][ind].print()

    # building horizontally    ^
    # -------------------------------------------
    # building vertically    v


    for j in range(len(final_build[0])):
        ind = 0
        while get_neighbor(final_build[ind][j].id, final_build[ind][j].south, reverse) is not None:
            adj_tile = actual_tiles[get_neighbor(final_build[ind][j].id, final_build[ind][j].south, reverse)]

            ind += 1
            if ind not in final_build:
                final_build[ind] = dict()
            final_build[ind][j] = adj_tile
            adj_tile.get_side_to(str_flip(final_build[ind-1][j].south), "north")
            # final_build[ind][0].print()

    # now deleting borders
    for i in range(len(final_build)):
        for j in range(len(final_build)):
            final_build[i][j].delete_border()

    final_puzzle = convert_to_txt(final_build)
    # print(final_puzzle)

    puz = convert_txt_to_numpy(final_puzzle)


    for i in range(4):
        # print(puz)
        sea, ans = count_sea_monsters(puz)
        if sea != 0:
            return ans
        else:
            puz = np.rot90(puz, 3)

    puz = np.fliplr(puz)

    for i in range(4):
        # print(puz)
        sea, ans = count_sea_monsters(puz)
        if sea != 0:
            return ans
        else:
            puz = np.rot90(puz, 3)




f_name = sys.argv[1]
print(solution(f_name))
