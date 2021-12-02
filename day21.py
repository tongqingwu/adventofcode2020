import re


class Allergen:
    def __init__(self, input):
        self.food_list = []  # list of dict, 'fish': {'sfsfsll', 'mdmdm'}, 'soy': same as fish, but need to be updated with other dict for fish, remove not common one. until find only one common for all food.
        self.d_aller = dict() # only one aller:, but list of ingred.  The final is one to one. must be {"soy" : {"sdfsf"}, "peanut": {"sssss"}}
        self.ingred_list = []  # whole list of everything, for part one
        self.aller_set = set()  # all allers, get from input
        self.aller_ingred_set = set()   # real aller ingred, same size as above aller, but just ingred
        self.non_aller_ingred_list = []

        with open(input) as f:
            f_cnt = 0
            for line in f:
                tmp_dict = dict()
                f_cnt += 1
                # print('food list {}-----------------------------------------'.format(f_cnt))
                line = line.rstrip()
                r = re.search(r'^(.+\S+) \(contains (.+)\)$', line)
                if r:
                    allers = r.group(2).split(', ')
                    s_allers = set(allers)
                    self.aller_set.update(s_allers)

                    ins = r.group(1).split(' ')
                    s_ins = set(ins)

                    self.ingred_list = self.ingred_list + ins   # must be list for part one

                    for a in s_allers:
                        tmp_dict[a] = s_ins

                    self.food_list.append(tmp_dict)

    def find_d_allers_w_one_ingred(self):
        while True:
            self.find_d_allers_and_update_l_food()
            if len(self.aller_ingred_set) == len(self.aller_set):  # make sure we got all aller dict
                break

    def find_d_allers_and_update_l_food(self):
        self.check_one_aller_ingred()
        list_set_pair = []
        for i in range(len(self.food_list)):
            for j in range(len(self.food_list)):
                if i == j or {i, j} in list_set_pair:
                    continue
                list_set_pair.append({i, j})  # process only once one pair

                for k, v in self.food_list[i].items():
                    for kk, vv in self.food_list[j].items():
                        if k == kk and v is not None and vv is not None and len(v) > 1:   # both 'fish'
                            s_common_ingreds = v.intersection(vv)
                            self.food_list[i][k] = s_common_ingreds
                            self.food_list[j][kk] = s_common_ingreds

    def check_one_aller_ingred(self):
        for i in range(len(self.food_list)):
            for k, v in self.food_list[i].items():
                if k not in self.aller_ingred_set and v is not None and len(v) == 1:
                    ingred = list(v)[0]
                    self.update_aller_dict_and_set(k, ingred)
        self.remove_one_from_others()

    def remove_one_from_others(self):
        # remove it from others
        for dk, dv in self.d_aller.items():
            for i in range(len(self.food_list)):
                for k, v in self.food_list[i].items():
                    if dk != k and v is not None and dv in v and len(v) > 1:
                        self.food_list[i][k].remove(dv)

    def update_aller_dict_and_set(self, aller, ingred):
        self.d_aller[aller] = ingred
        self.aller_ingred_set.add(ingred)

    def find_non_aller_ingred(self):
        nai_cnt = 0
        for i in self.ingred_list:
            if i not in self.aller_ingred_set:
                nai_cnt +=1

        print('Part One: {}'.format(nai_cnt))

    def part2(self):
        v_list = []
        for key in sorted(self.d_aller):
            v_list.append(self.d_aller[key])
        print(','.join(v_list))


allergen = Allergen('day21.txt')
allergen.find_d_allers_w_one_ingred()
allergen.find_non_aller_ingred()
allergen.part2()

     
