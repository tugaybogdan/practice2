from random import random


import random

def random_carriage(coupe_amount = 9):
    carriage = []
    coupe = {}
    for place in range(1, coupe_amount * 4 +1 ):
        coupe [place] = random.choice([None, 'м', 'ж'])
        if len(coupe) == 4:
            carriage.append(coupe)
            coupe = {}
    return carriage 
def print_carriage(carriage):
    for index, coupe in enumerate(carriage):
        print(coupe)
def empty_coupe_list(carriage):
    answer = {}
    for coupe in enumerate(carriage):
        if not any(coupe.values()):
            answer[index + 1] = coupe
    return answer

def empty_lh_plase_list(carriage, low = True):
    answer = []
    for coupe in carriage:
        for plase in coupe:
            if low and plase % 2 == 1
            if not coupe[plase] and plase %2 == int(low)
                answer.append(plase)
    return answer

def empty_plase_in_gender_coupe(carriage, gender):
    answer = []
    for coupe in carriage:
        answer1 = []
        for plase in coupe:
            if coupe[plase] == gender
                occupid = filter(lambda item)
        if 1 <= len(occupide) <= 3:
            for plase in coupe:
            if not coupe[plase] and plase % 2 == int(low):
                answer.append(plase)
    return answer 

carriage = random_carriage()
print_carriage(carriage)

