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

# 다른 풀이
def recursive(numbers, sum, target) :
    if numbers == [] :
        if sum == target :
            return 1
        else :
            return 0
    return recursive(numbers[1:], sum + numbers[0], target) + recursive(numbers[1:], sum - numbers[0], target)

def solution2(numbers, target) :
    return recursive(numbers, 0, target)