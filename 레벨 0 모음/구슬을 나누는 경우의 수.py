# 시간초과 코드
from itertools import combinations

def solution1(balls, share):
    combi = combinations(list(range(balls)), share)
    combi_list = list(combi)
    return len(combi_list)

solution1(3, 2)

# 모듈만 바꿈
import math

def solution(balls, share):
    return math.comb(balls, share)