import copy
def solution(bandage, health, attacks):
    answer = 0
    time = attacks[0][0]
    count = 0
    attack_num = 0
    # 깊은 복사
    full = copy.deepcopy(health)
    while time < attacks[-1][0]+1:
        if time == attacks[attack_num][0]:
            health -= attacks[attack_num][1]
            count = 0
            attack_num += 1
        else:
            health += bandage[1]
            count += 1
            if count == bandage[0]:
                health += bandage[2]
                count = 0
        if health > full:
            health = full
        if health <= 0 :
            return -1
        time += 1
    return health

