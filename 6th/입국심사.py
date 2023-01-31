# 입국심사대 개수 == len(times)
# 기다리는 사람 수 == n
# 심사하는데 걸리는 시간이 담긴 배열 times

def solution(n, times):
    
    start = 1
    end = max(times) * n
    res = max(times) * n

    while start <= end :
        mid = (start + end) // 2
        people = 0
        for time in times :
            people += (mid // time)
            
        if people < n :
            start = mid + 1
        
        else :
            end = mid -1
            res = min(res, mid)
    
    return res