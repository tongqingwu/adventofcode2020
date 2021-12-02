import re
import copy
import math


"""
1. use dict of sets like { '9': {'11', '12'}} to track and replace '1-9' of rules with 'a' and 'b'
2. after the set is empty, start to multiple  '8 9' and plus the rules. ' 8 | 9'
3. part two: pattern match to make sure the front is r42r42, end is r31, build patter with {num, } as minimum
   math.ceil is used as well to find the minimum for front matching.
"""


def get_lists(str_nums):
    """
    Only for parser, the first step to get all rules dictionary value
    :param str_nums:
    :return:
    """
    tmp_rules = []
    l_v = str_nums.split('|')
    for v in l_v:
        tmp_list = v.split(' ')
        if '' in tmp_list:
            tmp_list.remove('')
        tmp_rules.append(tmp_list)
    return tmp_rules


def get_list_m_list_times(l_strs, times):
    if times == 0:
        return l_strs
    else:
        ls_2 = l_strs
        ls_1 = l_strs
        while times > 0:
            ls_1 = get_list_m_list(ls_1, ls_2)
            times -= 1
        return ls_1


def get_list_m_list(l1, l2):
    """

    :param l1: ['aa', 'ab']
    :param l2: ['ba', 'bb']
    :return: ['aaba', 'abbb', 'aabb', 'abbb']
    """
    tmp_strs = []
    for i in l1:
        for j in l2:
            tmp_strs.append(i + j)
    return tmp_strs


class MonsterMessage:
    def __init__(self, l_input):
        self.d_num = dict()  # value is list of list [[1, 2, 5]] or [ [12, 1], [3, 1]] or [[14, 5]]
        # 28 14 is multiple, 14 | 16 is plus ONLY
        self.d_abs = dict()  # value is list of letters [ ab, baaaaa ] or ['a']
        self.d_num_set = dict()  # {rule: set(rules}, so we only get same rule ONLY once, like 3 and 2,
        self.d_num_set_cp = dict()
        self.l_msgs = []  # rule 0 msgs abaa
        self.l_msgs_d_len = dict()
        self.zero_msg_cnt = 0
        with open(l_input) as f:
            y = 0
            for line in f:
                line = line.rstrip()
                r = re.search(r'^(\d+): (.+)$', line)
                z = re.search(r'^[ab]', line)
                if z:
                    self.l_msgs.append(line)
                    len_line = len(line)
                    if len_line in self.l_msgs_d_len.keys():
                        self.l_msgs_d_len[len_line].append(line)
                    else:
                        self.l_msgs_d_len[len_line] = [line]
                elif r:
                    rule = r.group(1)
                    r_value = r.group(2)
                    if 'a' in r_value or 'b' in r_value:
                        self.d_abs[rule] = [r_value.replace('\"', '')]  # singleton list
                    else:
                        self.get_lists(rule, r_value)

        self.d_num_set_cp = self.d_num_set.copy()

        def get_lists(self, rule, str_nums):
        """
        Only for parser, the first step to get all rules dictionary value
        :param str_nums:
        :return:
        """
        tmp_set = set()
        tmp_rules = []
        l_v = str_nums.split('|')
        for v in l_v:
            tmp_list = v.split(' ')
            if '' in tmp_list:
                tmp_list.remove('')
            for t in tmp_list:
                tmp_set.add(t)
            tmp_rules.append(tmp_list)
        self.d_num[rule] = tmp_rules
        self.d_num_set[rule] = tmp_set

    def find_all_let_rule(self):
        while len(self.d_num_set) > 0:
            self.find_match_abs_and_update()

    def find_match_abs_and_update(self):
        cp_d_num_set = self.d_num_set.copy()  # copy for checking, update real one
        for k_n, v_n in cp_d_num_set.items():
            s_abs = set(self.d_abs.keys())
            if len(v_n - s_abs) == 0:
                # print('rule {} has all covered'.format(k_n))
                self.update_with_abs(k_n)  # update d_num

    def update_multiple_lists(self, m_list):  # not pipe at all just multiple to each ohter or single rule
        len_rule_list = len(m_list)
        if len_rule_list == 1:
            # print('only one rule, just replace it with ab')
            m_list = self.d_abs[m_list[0]]
        else:
            if len_rule_list == 2:
                m_list = get_list_m_list(self.d_abs[m_list[0]], self.d_abs[m_list[1]])
            else:
                # print('!!!!!!!!!!!!!! 3 multiple !!!!!!!!!!!!!!!!')
                for i in range(len(m_list)):
                    m_list[i] = self.d_abs[m_list[i]]

                tmp_list = [get_list_m_list(m_list[0], m_list[1])]
                if len(m_list) > 2:
                    tmp_list[1:1] = m_list[2:]
                m_list = tmp_list.copy()

                m_list = get_list_m_list(m_list[0], m_list[1])

        return m_list

   def update_with_abs(self, rule):
        tmp_list = self.d_num[rule]
        if len(tmp_list) == 1:
            tmp_list = self.update_multiple_lists(tmp_list[0])
        else:
            tmp_list[0] = self.update_multiple_lists(tmp_list[0])
            tmp_list[1] = self.update_multiple_lists(tmp_list[1])

            tmp_list = tmp_list[0] + tmp_list[1]

        self.d_num.pop(rule)
        self.d_abs[rule] = tmp_list
        self.d_num_set.pop(rule)

    def find_zero_match(self):
        print('Part one: ')
        print(len(set(self.l_msgs).intersection(set(self.d_abs['0']))))

    def part2(self):
        len_r42 = len(self.d_abs['42'][0])
        len_r31 = len(self.d_abs['31'][0])
        r31base = '(' + '|'.join(self.d_abs['31']) + '){1,}'
        for k, v in self.l_msgs_d_len.items():
            min_repeat_num_for_r42 = math.ceil((k - len_r42) / (len_r31 + len_r42)) + 1
            r42base = '(' + '|'.join(self.d_abs['42']) + ')' + '{' + str(min_repeat_num_for_r42) + ',}'
            pattern = re.compile(r'' + r42base + r31base)
            for msg in v:
                if re.fullmatch(pattern, msg):
                    self.zero_msg_cnt += 1
        print('Part two: {}'.format(self.zero_msg_cnt))


mm = MonsterMessage('day19.txt')
mm.find_all_let_rule()
mm.find_zero_match()

mm.part2()
