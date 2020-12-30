from itertools import cycle


class CrabCups:
    def __init__(self, input, add_to=0):  # add element till cnt num, 0 means no adding ( for part one)
        self.d_list = dict()

        tmp_list = []
        for i in list(input):
            tmp_list.append(int(i))
        self.max = max(tmp_list)
        self.min = min(tmp_list)

        # part two
        if add_to > self.max:
            for i in range(self.max + 1, add_to + 1):
                tmp_list.append(i)
            self.max = add_to

        # make a linked list { current: next }
        len_tmp_list = len(tmp_list)
        for i in range(len_tmp_list - 1):
            self.d_list[tmp_list[i]] = tmp_list[i + 1]
        self.d_list[tmp_list[len_tmp_list-1]] = tmp_list[0]

        # get values from dict !
        self.current = tmp_list[0]  # first label value
        self.destination = -1
        self.pick1 = -1
        self.pick2 = -1
        self.pick3 = -1
        self.pick_up = []

        # self.get_result()

    def get_destination(self):
        if self.max < 10:
            self.max = max(set(self.d_list.keys() - set(self.pick_up)))

        d = self.current - 1
        if d < self.min:
            self.destination = self.max
        else:
            if d in self.pick_up:
                while d in self.pick_up:
                    d -= 1
                    if d < self.min:
                        self.destination = self.max
                        return
                self.destination = d
            else:
                self.destination = d

    def get_result(self, label=1, part_two=False):
        after_label = self.d_list[label]
        list_after_label = [after_label]
        while True:
            after_label = self.d_list[after_label]
            list_after_label.append(after_label)
            if part_two:
                print('Part two: {}'.format(list_after_label[0] * list_after_label[1]))
                break
            if after_label == label:
                print('Part one: {}'.format(''.join([str(list_after_label[i])
                break

    def one_move(self):
        # print('Before move, current {}'.format(self.current))
        self.pick1 = self.d_list[self.current]
        self.pick2 = self.d_list[self.pick1]
        self.pick3 = self.d_list[self.pick2]
        self.pick_up = [self.pick1, self.pick2, self.pick3]

        self.get_destination()  # update destination.
        # print('Destination : {}'.format(self.destination))
        # print('Pick up: {}'.format(self.pick_up))

        # after insert back
        if self.d_list[self.pick3] == self.destination:
            self.d_list[self.current] = self.destination
        else:
            self.d_list[self.current] = self.d_list[self.pick3]

        self.d_list[self.pick3] = self.d_list[self.destination]
        self.d_list[self.destination] = self.pick1
        self.current = self.d_list[self.current]
        # self.get_result()

    def move(self, move_cnt):
        cnt = 0
        while cnt < move_cnt:
            cnt += 1
            # print('Move cnt : {} '.format(cnt))
            self.one_move()


# part 1:
# cc = CrabCups('389125467')  # example
cc = CrabCups('952316487')  # real
cc.move(100)
cc.get_result()

# part 2:
cc = CrabCups('952316487', add_to=1000000)
cc.move(10000000)
cc.get_result(part_two=True)
