import re


def is_valid(f_i, v):
    if v[0] <= f_i <= v[1] or v[2] <= f_i <= v[3]:
        return True
    else:
        return False

                    
class Tickets:
    def __init__(self, input):
        self.input = input
        self.fields = dict()
        self.cols_fs = []  # col 0:[fields_name]
        self.list_ones = []  # col index list has ONLY one field name
        self.not_ones = []
        self.valid_ts = []  # list of tks
        self.your_tk = []

    def scan(self):
        is_yours = True
        total_cnt = 0
        rate = 0
        with open(self.input) as f:
            for line in f:
                line = line.rstrip()
                d = re.search(r'^(.+): (\d+)-(\d+) or (\d+)-(\d+)', line)
                if d:
                    self.fields[d.group(1)] = [int(d.group(2)), int(d.group(3)), int(d.group(4)), int(d.group(5))]

                m = re.search(r'your ticket', line)
                n = re.search(r'nearby', line)
                t = re.search(r'(\d+),(\d+),(\d+)', line)
                if m:
                    is_yours = True
                if n:
                    is_yours = False

                if t:
                    flds = []
                    for f in line.split(','):
                        flds.append(int(f))

                    if is_yours:
                        self.cols_fs = self.get_fields_for_col(flds)
                        self.your_tk = flds
                    else:
                        total_cnt += 1
                        e_rate = self.scan_fields_for_col(flds)

                        if e_rate == 0:
                            self.valid_ts.append(flds)
                        else:
                            rate += e_rate

        print('Total nearby tks {} and valid {}'.format(total_cnt, len(self.valid_ts)))
        print('Part one: {}'.format(rate))

    def get_fields_for_col(self, flds):
        tmp_cols = []
        for i in range(len(flds)):
            f_i = flds[i]
            tmp_p = []
            for k, v in self.fields.items():
                if is_valid(f_i, v):
                    tmp_p.append(k)

            tmp_cols.append(tmp_p)
        return tmp_cols

    def update_cols_fs_with_ones(self):
        for i in range(len(self.cols_fs)):
            if len(self.cols_fs[i]) == 1:
                self.list_ones.append(i)
            else:
                self.not_ones.append(i)

        list_ones_cnt = len(self.list_ones)
        while True:
            new_list_ones_cnt = self.update_ones()
            if new_list_ones_cnt == list_ones_cnt:
                break
            else:
                list_ones_cnt = new_list_ones_cnt

    def update_ones(self):
        new_list_ones = self.list_ones.copy()
        new_not_ones = self.not_ones.copy()
        for n_o in self.not_ones:
            for i_o in self.list_ones:
                if self.cols_fs[i_o][0] in self.cols_fs[n_o]:
                    self.cols_fs[n_o].remove(self.cols_fs[i_o][0])

            if len(self.cols_fs[n_o]) == 1:
                new_list_ones.append(n_o)
                new_not_ones.remove(n_o)

        self.list_ones = new_list_ones.copy()
        self.not_ones = new_not_ones.copy()

        return len(new_list_ones)

    def scan_fields_for_col(self, flds):
        rates = []
        rate = 0
        for i in range(len(flds)):
            has_error = True
            f_i = flds[i]
            for f_p in self.cols_fs[i]:
                if is_valid(f_i, self.fields[f_p]):
                    has_error = False
                    break
            if has_error:
                rates.append(f_i)

        for r in rates:
            rate += r
        return rate

    def part2(self):
        for flds in self.valid_ts:
            self.update_cols_fs(flds)
            
        self.update_cols_fs(self.your_tk)

        self.update_cols_fs_with_ones()

        print('AFTER set: {}'.format(self.cols_fs))
        print('Part two: {}'.format(self.get_deps_yours()))

    def get_deps_yours(self):
        m = 1
        for i in range(len(self.your_tk)):
            f_i = self.your_tk[i]
            v = self.cols_fs[i]
            d = re.search(r'departure', v[0])
            if d:
                m *= f_i
                    
        return m
                
    def update_cols_fs_new(self, flds):
        tmp_cols = self.get_fields_for_col(flds)
        for i in range(len(flds)):
            common_set = set(tmp_cols[i]).intersection(self.cols_fs[i])
            self.cols_fs[i] = list(common_set)

    def update_cols_fs(self, flds):
        new_cols_fs = self.cols_fs.copy()
        for i in range(len(flds)):
            f_i = flds[i]
            for f_p in new_cols_fs[i]:
                if not is_valid(f_i, self.fields[f_p]):
                    new_cols_fs[i].remove(f_p)
         
        self.cols_fs = new_cols_fs.copy()
        

tks = Tickets('day16.txt')
tks.scan()
tks.part2()
