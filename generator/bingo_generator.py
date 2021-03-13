import pandas as pd
import numpy as np
import time

from generator.utility.score_checker import total_card_score
from generator.utility.image_util import bingo_table_to_image
from generator.cls.bingo_table import BingoTable

def random_table_gen(source_list):
    table = []
    np.random.shuffle(source_list)
    for i in range(0, 5): # rows
        row = []
        for j in range(0, 5): # columns
            if i == 2 and j == 2:
                row.append("FREE")
            else:
                row.append(source_list[(i * 5) + j])
        table.append(row)
    return table

# def generate_all_tables(values, tablenum):
#     tables = []
#     while len(tables) < tablenum:
#         cur_list = random_table_gen(values)
#         if len(tables) == 0:
#             tables.append(cur_list)
#         else:
#             bool_sum = False
#             for arr in tables:
#                 # The score here is a highly unscientific 21.
#                 # We should calculate this.
#                 bool_sum += bingo_match_score_exceed(np.ravel(cur_list), np.ravel(arr), 21)
#             if not bool_sum:
#                 tables.append(cur_list)
#     return tables

def generate_all_tables(values, tablenum):
    tables = []
    iter_num = 0
    while len(tables) < tablenum:
        iter_num += 1
        start_time = time.time()
        cur_tbl = BingoTable(random_table_gen(values), iter_num, len(tables) + 1)
        if len(tables) == 0:
            tables.append(cur_tbl)
        else:
            bool_sum = False
            for tbl in tables:
                for win_state in tbl.win_states:
                    bool_sum += cur_tbl.check_win_state_match(win_state)
            
            if not bool_sum:
                cur_tbl.gen_time = time.time() - start_time
                tables.append(cur_tbl)
            else:
                del cur_tbl
    return tables

def create_bingo_cards(values, card_num):
    tables = generate_all_tables(values, card_num)
    score = 0
    for indx in range(len(tables)):
        tbl = tables[indx]
        score = total_card_score(tbl, tables[:indx] + tables[indx+1:])
        tbl_id = tbl.set_score_and_get_id(score)
        bingo_table_to_image(tbl.table, "output/{}.png".format(tbl_id), tbl_id)


