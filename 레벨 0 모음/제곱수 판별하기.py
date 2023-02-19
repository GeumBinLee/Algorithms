# 내 풀이 1
import math
def solution(n):
    return 1 if math.sqrt(n).is_integer() else 2

# 내 풀이 2 -> 사실상 모듈 유무 차이 정도밖엔
def solution(n):
    return 1 if (n**(1/2)).is_integer() else 2