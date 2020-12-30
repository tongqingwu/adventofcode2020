import re

class CrabGame:
    def __init__(self, input):
        self.cards = []  # {id: []
        self.num = 0

        with open(input) as f:
            tmp_list = []
            for line in f:
                line = line.rstrip()
                m = re.search(r'^(\d+)$', line)
                t = re.search(r'Player (\d)', line)

                if t:
                    if t.group(1) == '2':
                        self.cards.append(tmp_list)
                        tmp_list = []
                if m:
                    tmp_list.append(int(m.group(1)))

            self.cards.append(tmp_list)
            print('{}'.format(self.cards))
            self.num = len(self.cards[0])
            print('num is {}'.format(self.num))

    def play(self):
        wins = []
        while True:
            self.one_round()
            if len(self.cards[0]) == self.num * 2:
                wins = self.cards[0]
                break
            elif len(self.cards[1]) == self.num * 2:
                wins = self.cards[1]
                break

        print('wins {}'.format(wins))
        wins.reverse()
        m = 0
        for i in range(self.num * 2):
            print('i {}, wins {}'.format(i, wins[i]))
            m += (i + 1) * wins[i]

        print('Part one: {}'.format(m))

    def one_round(self):
        c1 = self.cards[0].pop(0)
        c2 = self.cards[1].pop(0)

        print('c1 {}, c2 {}'.format(c1, c2))

        if c1 > c2:
            self.cards[0].append(c1)
            self.cards[0].append(c2)
        else:
            self.cards[1].append(c2)
            self.cards[1].append(c1)

        print('cards {}'.format(self.cards))


cg = CrabGame('day22.txt')
cg.play()

