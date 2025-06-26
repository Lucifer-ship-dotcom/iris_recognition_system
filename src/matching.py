import numpy as np

def hamming_distance(feature1, feature2):
    return np.sum(feature1 != feature2) / len(feature1)

def match_iris(feature, database):
    best_match = None
    lowest_score = 1.0
    for name, db_feature in database.items():
        score = hamming_distance(feature, db_feature)
        if score < lowest_score:
            best_match = name
            lowest_score = score
    return best_match, lowest_score
