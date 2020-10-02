'''
Natural Language Processing (NLP)
ECOM6355

ASSIGNEMENT # 2

AZIZA AWAD HASSAN
220182085

'''


#import Levenshtein
import numpy as np
import random
import string

def edit_distance(s, t):
    print(s)
    print(t)

    s = s.split()
    t = t.split()

    print(s)
    print(t)

    edit_distance_matrix = np.zeros((len(s) + 1, len(t) + 1))
    #edit_distance_matrix[:, 0] = list(range(len(s) + 1))
    #edit_distance_matrix[0, :] = list(range(len(t) + 1))

    edit_distance_matrix[:, 0] = range(len(s) + 1)
    edit_distance_matrix[0, :] = range(len(t) + 1)

    print(edit_distance_matrix)

    for i in range(1, len(s) + 1):
        for j in range(1, len(t) + 1):
            insertion = edit_distance_matrix[i, j - 1] + 1
            deletion = edit_distance_matrix[i - 1, j] + 1
            substitution = edit_distance_matrix[i - 1, j - 1]
            if s[i - 1] != t[j - 1]:
                substitution += 2  # -- mismatch
            edit_distance_matrix[i, j] = min(insertion, deletion, substitution)
    print(edit_distance_matrix)
    return int(edit_distance_matrix[i, j])


print(edit_distance('welcome! I am Eng. Aziza Hassan','Welcome! I am Aziza Awad Hassan'))