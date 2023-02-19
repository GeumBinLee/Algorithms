# 내 풀이
def solution(n, t):
    return n*(2**t)

# 다른 풀이 -> 비트시프트 사용
# 처음 들어봤당 비트시프트
def solution(n, t):
    return n << t