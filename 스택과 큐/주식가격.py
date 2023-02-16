# 효율성 검사 통과 못한 풀이 (시간 초과)
def solution1(prices) :
    answer = []
    
    while prices :
        answer.append(0)
        for price in prices[1:] :
            if prices[0] <= price :
                answer[-1] += 1
            else :
                answer[-1] += 1
                break
        del prices[0]
    print(f"answer = {answer}, prices = {prices}")
    
    return answer

# 프린트문 없애면 통과, 프린트문 있으면 출력 크기 초과로 실패
from collections import deque
def solution(prices) :
    answer = []
    queue = deque(prices)
    
    while queue :
        first = queue.popleft()
        sec = 0
        
        for q in queue :
            if first <= q :
                sec += 1
            else :
                sec += 1
                break
        answer.append(sec)
    
    print(f"answer = {answer}, prices = {prices}")
    return answer

# 다른 사람 풀이
def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i, len(prices)-1):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                break

    return answer



solution([1,2,3,2,3])