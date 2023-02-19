# 내 풀이 : range(n)으로 하고 마지막에 +1 안 한 거랑 똑같음
def solution(n):
    common_divisor = set()
    for i in range(1, n//2+1) :
        if n % i == 0 :
            common_divisor.add((i, n//i))
    return len(common_divisor) + 1

# 다른 풀이
def solution(n):
    return len(list(filter(lambda v: n % (v+1) == 0, range(n))))