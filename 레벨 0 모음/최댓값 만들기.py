# 내 풀이
from itertools import combinations

def solution(numbers):
    combi = list(combinations(numbers, 2))
    return max([x[0]*x[1] for x in combi])

# 다른 풀이
def solution(numbers):
    numbers = sorted(numbers)
    return max(numbers[0] * numbers[1], numbers[-1]*numbers[-2]) 
