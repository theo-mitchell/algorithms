'''
Maria plays college basketball and wants to go pro. 
Each season she maintains a record of her play. 
She tabulates the number of times she breaks her season record for most points and least points in a game. 
Points scored in the first game establish her record for the season, and she begins counting from there.

Ex: scores = [12, 10, 3, 5, 10]

Given the scores for a season, determine the number of times Maria breaks her records for most and least points scored during the season.
'''


def breakingRecords(scores):
    min = scores.pop(0)
    max = min 
    
    minBroken = 0 
    maxBroken = 0
    
    for score in scores:
        if score > max:
            max = score
            maxBroken += 1
        
        if score < min:
            min = score
            minBroken += 1
    
    return [maxBroken, minBroken]