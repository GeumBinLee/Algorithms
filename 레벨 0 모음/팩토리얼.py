def solution(n):
    answer = 0
    factorial = 1
    while (n>=factorial): 
        answer += 1
        factorial = factorial * answer

    return answer - 1

# 다른 풀이 : math 모듈의 factorial 메소드 사용
from math import factorial

def solution(n):
    k = 10
    while n < factorial(k):
        k -= 1
    return k