# 내 풀이
def solution(array, n):
    answer = 0
    for arr in array :
        if arr == n :
            answer += 1
    return answer

# 다른 풀이
def solution(array, n):
    return array.count(n)