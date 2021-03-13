def bingo_match_score_exceed(arr1, arr2, score_limit=21):
    score = 0
    for i in range(0, len(arr1)):
        if arr1[i] == 'FREE':
            pass
        elif arr1[i] == arr2[i]:
            score += 5
        elif arr1[i] in arr2:
            score += 1
        else:
            score += 0
        
        if score > score_limit:
            return True
    return False

def ind_bingo_table_score(arr1, arr2):
    score = 0
    
    for i in range(0, len(arr1)):
        if arr1[i] == 'FREE':
            pass
        elif arr1[i] == arr2[i]:
            score += 5
        elif arr1[i] in arr2:
            score += 1
        else:
            score += 0
        
    return score

def total_card_score(tbl, list_of_tbls):
    score_sum = 0
    for comp_tbl in list_of_tbls:
        score_sum += ind_bingo_table_score(tbl.flattened_table, comp_tbl.flattened_table)

    return score_sum