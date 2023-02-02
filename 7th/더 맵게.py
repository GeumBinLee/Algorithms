# 효율성 검사 통과 못한 답안
def solution1(scoville, K):
    answer = 0
    
    while min(scoville) < K :
        answer += 1
        scoville.sort()
        scoville.append(scoville[0]+(scoville[1]*2))
        del scoville[0:2]
        
        if len(scoville) == 1 and scoville[0] < K :
            return -1
        
    return answer

def solution2(scoville, K):
    answer = 0
    
    while min(scoville) < K :
        answer += 1
        
        min1 = min(scoville)
        scoville.remove(min1)
        min2 = min(scoville)
        scoville.remove(min2)
        
        scoville.append(min1+min2*2)
        
        if len(scoville) == 1 and min(scoville) < K :
            return -1
        
    return answer

# 통과 코드
from heapq import heappop
from heapq import heappush
from heapq import heapify

def solution(scoville, K) :
    count = 0
    heapify(scoville)
    while scoville[0] < K and len(scoville) > 1 :
        num1 = heappop(scoville)
        num2 = heappop(scoville)
        heappush(scoville, num1 + num2 * 2)
        count += 1
        if scoville[0] >= K :
            print(count)
            return count
        else :
            return -1

solution([1, 2, 3, 9, 10, 12], 7)