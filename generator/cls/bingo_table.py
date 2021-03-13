import numpy as np

class BingoTable:

    def __init__(self, table, iter_num, card_num):
        self.table = table
        self.gen_iteration = iter_num
        self.gen_time = 0
        self.card_num = card_num
        self.flattened_table = np.ravel(table)

        self.win_states = self.generate_win_states()

    def generate_win_states(self):
        # Generates the 12 possible win states on a bingo card
        win_states = []

        # get list of columns
        for x in range(5):
            win_states.append([self.table[x][y] for y in range(5)])

        # get list of columns
        for y in range(5):
            win_states.append([self.table[x][y] for x in range(5)])

        # get diagonals
        win_states.append([
            self.table[0][0],
            self.table[1][1],
            self.table[2][2],
            self.table[3][3],
            self.table[4][4]])
        
        win_states.append([
            self.table[0][4],
            self.table[1][3],
            self.table[2][2],
            self.table[3][1],
            self.table[4][0]])


        return win_states

    def check_win_state_match(self, check_row):
        check_set = set(check_row)
        for state in self.win_states:
            if set(state) == check_set:
                return True
        return False

    def set_score_and_get_id(self, score):
        self.score = score
        self.id = "{}-{}-{}".format(str(self.gen_iteration), str(self.card_num), str(self.score))
        return self.id