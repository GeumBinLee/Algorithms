from itertools import permutations

def solution(babbling) :
    answer = 0
    can = ["aya", "ye", "woo", "ma"]
    perm = []
    
    for i in range(1, len(can) +1) :
        for p in permutations(can, i) :
            perm.append("".join(p))
    
    for b in babbling :
        if b in perm :
            answer += 1
    return answer

# 오 다른 사람 풀이랑 아예 똑가틈 기분 져아
    

solution(["aya", "yee", "u", "maa", "wyeoo"])