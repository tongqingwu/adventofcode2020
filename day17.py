import re

ACT = '#'
INC = '.'


class Cubes:
    def __init__(self, input):
        self.input = input
        self.d_cubes = dict()  # {(tuple): True } ex. (1,2,3):'#'', is an active cube
        
    def start(self):
        with open(self.input) as f:
            y = 0
            for line in f:
                line = line.rstrip()
                len_line = len(line)
                for x in range(len_line):
                    cube = (x, y, 0)
                    self.d_cubes[cube] = line[x]
                y += 1

        for i in range(-1, len_line+2):
            for j in range(-1, y+1):
                for k in range(-1, 3):
                    t = (i, j, k)
                    if t not in self.d_cubes:
                        self.d_cubes[t] = INC

        cubes_cnt = len(self.d_cubes)
        print('d_cube size {}'.format(cubes_cnt))
        # print('Total Active: {}'.format(self.cnt_active()))
        # self.show_z()

    def count_neigbour(self, k, cp_dict):
        cnt = 0
        n_cnt = 0
        x = k[0]
        y = k[1]
        z = k[2]

        for i in (x - 1, x, x + 1):
            for j in (y - 1, y, y + 1):
                for k in (z - 1, z, z + 1):
                    if i != x or j != y or k != z:
                        n_cnt += 1
                        if self.check_cube_active((i, j, k), cp_dict):
                            cnt += 1

        return cnt

    def check_cube_active(self, t, cp_dict):
        # bad code here:
        # if t in cp_dict and cp_dict[t] == ACT:
        #         return True
        if t in cp_dict:
            if cp_dict[t] == ACT:
                return True
            else:
                return False
        else:  # ONLY expend the current cubes
            self.d_cubes[t] = INC
            return False

    def one_cycle(self):
        # print('Before this cycle, size {}'.format(len(self.d_cubes)))
        cp_dict = self.d_cubes.copy()

        for k, v in cp_dict.items():
            active_cnt = self.count_neigbour(k, cp_dict)
            if v == ACT:
                if active_cnt == 3 or active_cnt == 2:
                    self.d_cubes[k] = ACT
                else:
                    self.d_cubes[k] = INC
            else:
                if active_cnt == 3:
                    self.d_cubes[k] = ACT
                else:
                    self.d_cubes[k] = INC
        # self.show_z()
        print('Total Active after this cycle: {}'.format(self.cnt_active()))

    def show_z(self):
        print('z=-1')
        print('{}{}{}'.format(self.d_cubes[(0,0,-1)], self.d_cubes[(1,0,-1)], self.d_cubes[(2,0,-1)]))
        print('{}{}{}'.format(self.d_cubes[(0,1,-1)], self.d_cubes[(1,1,-1)], self.d_cubes[(2,1,-1)]))
        print('{}{}{}'.format(self.d_cubes[(0,2,-1)], self.d_cubes[(1,2,-1)], self.d_cubes[(2,2,-1)]))
        
        print('z=0')
        print('{}{}{}'.format(self.d_cubes[(0,0,0)], self.d_cubes[(1,0,0)], self.d_cubes[(2,0,0)]))
        print('{}{}{}'.format(self.d_cubes[(0,1,0)], self.d_cubes[(1,1,0)], self.d_cubes[(2,1,0)]))
        print('{}{}{}'.format(self.d_cubes[(0,2,0)], self.d_cubes[(1,2,0)], self.d_cubes[(2,2,0)]))
        
        print('z=1')
        print('{}{}{}'.format(self.d_cubes[(0,0,1)], self.d_cubes[(1,0,1)], self.d_cubes[(2,0,1)]))
        print('{}{}{}'.format(self.d_cubes[(0,1,1)], self.d_cubes[(1,1,1)], self.d_cubes[(2,1,1)]))
        print('{}{}{}'.format(self.d_cubes[(0,2,1)], self.d_cubes[(1,2,1)], self.d_cubes[(2,2,1)]))

    def run_cycles(self, cycle_cnt):
        cnt = 0
        while cnt < cycle_cnt:
            cnt += 1
            self.one_cycle()
            # print('After circle {}, cube cnt {}'.format(cnt, len(self.d_cubes)))

    def cnt_active(self):
        cnt = 0
        for k, v in self.d_cubes.items():
            if v == ACT:
                cnt += 1
        return cnt


# cubes = Cubes('day17.txt')
cubes = Cubes('day17.txt')
cubes.start()
cubes.run_cycles(6)
    
