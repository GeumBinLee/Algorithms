from itertools import combinations

def solution(numbers, target):
    answer = 0
    
    combi_list = []
    for i in range(1, len(numbers)) :
        combi = list(combinations(numbers, i))
        combi_list += combi
    
    for x in combi_list :
        if sum(x) == (sum(numbers)-target)/2 :
            answer += 1
    
    return answer

solution([1,1,1,1,1], 3)