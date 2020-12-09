import re
import copy

instructions = []  # with step
instructions_act_only = []  # without step (never change) 
total_ins = 0 
acc = 0 
step = 0

NOP = 'nop'
JMP = 'jmp'


# list of [ [ 'nop +0'] , ...}
def get_instruction_from_file():
    global instructions_act_only
    with open('day8.txt') as f:
        for line in f:
            tmp_list = []
            line = line.rstrip()
            tmp_list.append(line)
            instructions_act_only.append(tmp_list)


# return next index and update current acc list # if current acc list > 2, return def update_acc_list_for_both_current_and_next_ins(current_ins_index):
def update_acc_list_for_both_current_and_next_ins(current_ins_index):
    global instructions
    global acc
    global step
    next_index = 0
    has_acc = False
    is_end = False

    tmp_list = instructions[current_ins_index]  # list of ins : ['acc =1']
    # print('Current index {} has list {}, ins>{}<'.format(current_ins_index, tmp_list, tmp_list[0]))
    ins = (tmp_list)[0]
    b = re.search(r'(\S+) (\S)(\d+)', ins)

    acc_before = acc

    step += 1
    if b:
        act = b.group(1)
        num = int(b.group(3))
        sign = b.group(2)
        if act == NOP:
            next_index = current_ins_index + 1
        elif act == 'acc':
            if sign == '+':
                acc += num
            else:
                acc -= num
            next_index = current_ins_index + 1
        elif act == JMP:
            if sign == '+':
                next_index = current_ins_index + num
            else:
                next_index = current_ins_index - num

    # update current
    tmp_list.append(str(step))
    instructions[current_ins_index] = tmp_list

    # print('Current index list : {} has ins, acc {}'.format(tmp_list, acc))
    # print('Next index {}'.format(next_index))

    if next_index == len(instructions):
        print('Got to end !!! Has acc {}'.format(acc))
        is_end = True
        exit(1)

    if len(tmp_list) > 2:
        print('Got it !!! Has acc {}'.format(acc_before))
        has_acc = True

    return has_acc, is_end, next_index


def find_acc():
    global instructions
    global acc
    global step
    acc = 0

    has_acc, is_end, index = update_acc_list_for_both_current_and_next_ins(0)
    while not has_acc and not is_end:
        has_acc, is_end, index = update_acc_list_for_both_current_and_next_ins(index)


def get_new_ins(new_act, ind):
    global instructions_act_only
    copy_ins = copy.deepcopy(instructions_act_only)
    copy_ins[ind] = [new_act]

    return copy_ins


def get_new_ins_list():
    global instructions_act_only
    ind = 0
    list_new_ins = []  # list of list ins has new act
    for i in instructions_act_only:
        act = i[0]
        if JMP in act:
            print('Find index {}'.format(ind))
            new_act = act.replace(JMP, NOP)
            list_new_ins.append(get_new_ins(new_act, ind))
        elif NOP in act:
            print('Find index {}'.format(ind))
            new_act = act.replace(NOP, JMP)
            get_new_ins(new_act, ind)
            list_new_ins.append(get_new_ins(new_act, ind))

        ind += 1

    return list_new_ins


def main():
    global instructions
    get_instruction_from_file()

    instructions = copy.deepcopy(instructions_act_only)
    # part 1
    # find_acc()

    # part 2
    # get all ins with one replacement ONLY
    list_new = get_new_ins_list()
    for l in list_new:
        # print('New ins ----- {}'.format(l))
        instructions = copy.deepcopy(l)  # ONLY has act
        find_acc()


if __name__ == '__main__':
    main()

