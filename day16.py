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
        self.cols_fs = dict()  # col 0:[fields_name]
        self.list_ones = [] # col index list has ONLY one field name
        self.not_ones = []

    def scan(self):
        is_yours = True
        total_cnt = 0
        rate = 0
        with open(self.input) as f:
            for line in f:
                line = line.rstrip()
                d = re.search(r'^(\S+): (\d+)-(\d+) or (\d+)-(\d+)', line)
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
                    flds = line.split(',')
                    if is_yours:
                        self.get_fields_for_col(flds)
                    else:
                        total_cnt += 1
                        rate += self.scan_fields_for_col(flds)

        print('Part one: {}'.format(rate))

    def get_fields_for_col(self, flds):
        for i in range(len(flds)):
            f_i = int(flds[i])
            print('f_i {}'.format(f_i))
            tmp_p = []
            for k, v in self.fields.items():
                print('k {}, v {}'.format(k, v))
                if is_valid(f_i, v): 
                    tmp_p.append(k)
            if len(tmp_p) == 1:
                self.list_ones.append(i)
            else:
                self.not_ones.append(i) 

            self.cols_fs[i] = tmp_p 

        print('no_ones: {}'.format(self.not_ones))
        print('li_ones: {}'.format(self.list_ones))

        list_ones_cnt = len(self.list_ones)
        while True:
            new_list_ones_cnt = self.update_ones()
            if new_list_ones_cnt == list_ones_cnt:  
                break
            else:
                list_ones_cnt = new_list_ones_cnt

        print('AFTER UPDAT: cols_fs {}'.format(self.cols_fs))
 
    def update_ones(self):
        print('UPDAT: cols_fs {}'.format(self.cols_fs))
        new_list_ones = self.list_ones.copy()
        new_not_ones = self.not_ones.copy()
        print('UPDATE NEW : not ones {}'.format(self.not_ones))
        for n_o in self.not_ones:
            for i_o in self.list_ones:
                print('n_o {}, i_o {}'.format(n_o, i_o))
                if self.cols_fs[i_o][0] in self.cols_fs[n_o]:
                    self.cols_fs[n_o].remove(self.cols_fs[i_o][0])

            if len(self.cols_fs[n_o]) == 1:
                new_list_ones.append(n_o)
                new_not_ones.remove(n_o)

        self.list_ones = new_list_ones.copy()
        self.not_ones = new_not_ones.copy()
   
        return len(new_list_ones) 

    def scan_fields_for_col(self, flds):
        print('fls_d {}'.format(self.fields))
        print('col_d {}'.format(self.cols_fs))
        rates = [] 
        rate = 0
        for i in range(len(flds)):
            print('Check column {}-----'.format(i))
            has_error = True
            f_i = int(flds[i])
            for f_p in self.cols_fs[i]:
                if is_valid(f_i, self.fields[f_p]):
                    has_error = False
                    break
            if has_error:
                print('All f failed for {}'.format(f_i))
                rates.append(f_i)

        for r in rates:
            print('rates: {}'.format(rates))
            rate += r
        return rate 

#tks = Tickets('d16.txt')
tks = Tickets('day16.txt')
tks.scan()


