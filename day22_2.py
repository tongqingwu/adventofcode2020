import re


class CrabGame:
    def __init__(self, input):
        self.cards = []  # {id: []
        self.num = 0
        self.dealt_cards = [] # list of card,
        self.game_winner = 0
        self.histories = [[],[]]  # list of list of list
        self.game_cnt = 0

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
            # print('{}'.format(self.cards))
            self.num = len(self.cards[0])
            # print('num is {}'.format(self.num))

    def play(self):
        self.game_cnt = 1
        wins = []

        new_c1s, new_c2s = self.game(self.cards[0], self.cards[1])

        if len(new_c2s) == self.num * 2:  # real winner, no break
            wins = new_c2s
        elif self.game_winner == 1 and len(new_c1s) > 0 :
            wins = new_c1s

        print('wins {}'.format(wins))
        wins.reverse()
        m = 0
        for i in range(len(wins)):
            m += (i + 1) * wins[i]

        print('Part two: {}'.format(m))

    def game(self, c1s, c2s):
        h1 = []
        h2 = []
        self.game_winner = 0
        count =0

        while True:
            count +=1
            # print('count= {}'.format(count))
            if c1s in h1 or c2s in h2:
                self.game_winner = 1
                break

            if len(c1s) == 0:
                self.game_winner = 2
                break
            elif len(c2s) == 0:
                self.game_winner = 1
                break

            h1.append(c1s.copy())
            h2.append(c2s.copy())

            # pop first
            c1 = c1s.pop(0)
            c2 = c2s.pop(0)

            if len(c1s) >= c1 and len(c2s) >= c2:
                self.game_cnt += 1
                new_c1s = c1s.copy()[:c1]
                new_c2s = c2s.copy()[:c2]
                new_c1s, new_c2s = self.game(new_c1s, new_c2s)
            else:
                if c1 > c2:
                    self.game_winner = 1
                else:
                    self.game_winner = 2

            if self.game_winner == 1:
                c1s.append(c1)
                c1s.append(c2)
            elif self.game_winner == 2:
                c2s.append(c2)
                c2s.append(c1)

        return c1s, c2s


cg = CrabGame('day22.txt')
cg.play()

