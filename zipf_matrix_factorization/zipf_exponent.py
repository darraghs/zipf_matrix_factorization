import numpy as np

from estimates import  estimate_rank

def find_max_rank( ranks ):
    """ Find the highest ranked item """
    max_rank  = 0
    for i in len(ranks):
        if ranks[i] > max_rank:
            max_rank = ranks[i]
    return max_rank


