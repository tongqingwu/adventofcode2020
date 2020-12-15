NEAR = 'near'
FAR = 'far'

class MemGame:
    def __init__(self, input, big_turn):
        self.input = input
        self.big_turn = big_turn
        self.d_nums = dict()
        self.turn = 0

    def update_dict(self, nm):
        if nm in self.d_nums.keys():
            if NEAR in self.d_nums[nm].keys():
                self.d_nums[nm][FAR] = self.d_nums[nm][NEAR]
        else:
            self.d_nums[nm] = dict() 
            
        self.d_nums[nm][NEAR] = self.turn 

    def check_dict(self):
        for nm in self.input:
            self.turn += 1
            self.update_dict(nm)
           
        c_num = self.input.pop()
        while True:
            n_num = self.find_next_num(c_num)
            self.turn += 1
            self.update_dict(n_num)
            if self.turn == self.big_turn:
                print('Turn {} has num {}'.format(self.turn, n_num))
                break
            c_num = n_num

            
    def find_next_num(self, c_num):
        if FAR in self.d_nums[c_num].keys():
            return self.d_nums[c_num][NEAR] - self.d_nums[c_num][FAR]
        else:
            return 0

mg = MemGame([20,9,11,0,1,2], 30000000)
# mg = MemGame([3,2,1], 2020)
mg.check_dict()
