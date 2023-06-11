#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    max_score = max(a_dictionary, key=lambda x: a_dictionary[x])
    return max_score
