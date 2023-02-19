# 내 풀이
def solution(n, numlist):
    return [x for x in numlist if x % n == 0]

# 다른 풀이 -> filter() 활용
def solution(n, numlist):
    return list(filter(lambda v: v%n==0, numlist))