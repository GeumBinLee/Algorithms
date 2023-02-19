def solution(box, n):
    return (box[0]//n)*(box[1]//n)*(box[2]//n)

# 다른 풀이 -> math 모듈 활용
import math

def solution(box, n):
    return math.prod(map(lambda v: v//n, box))