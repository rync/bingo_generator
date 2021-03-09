import pandas as pd
import numpy as np

from generator.utility.score_checker import bingo_match_score_exceed
from generator.utility.image_util import bingo_table_to_image

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

def generate_all_tables(values, tablenum):
    tables = []
    while len(tables) < tablenum:
        cur_list = random_table_gen(values)
        if len(tables) == 0:
            tables.append(cur_list)
        else:
            bool_sum = False
            for arr in tables:
            	# The score here is a highly unscientific 21.
            	# We should calculate this.
                bool_sum += bingo_match_score_exceed(np.ravel(cur_list), np.ravel(arr), 21)
            if not bool_sum:
                tables.append(cur_list)
    return tables

def create_bingo_cards(values, card_num):
	tables = generate_all_tables(values, card_num)
	for i in range(len(tables)):
		bingo_table_to_image(tables[i], "output/{}.png".format(i))


