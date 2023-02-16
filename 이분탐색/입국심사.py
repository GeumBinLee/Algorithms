# 입국심사대 개수 == len(times)
# 기다리는 사람 수 == n
# 심사하는데 걸리는 시간이 담긴 배열 times

def solution(n, times):
    answer = 0
    # right는 가장 비효율적으로 심사했을 때 걸리는 시간
    # 가장 긴 심사시간이 소요되는 심사관에게 n 명 모두 심사받는 경우이다.
    left, right = 1, max(times) * n
    while left <= right:
        print(left, right)
        mid = (left+ right) // 2
        people = 0
        for time in times:
            # people 은 모든 심사관들이 mid분 동안 심사한 사람의 수
            people += mid // time
            # 모든 심사관을 거치지 않아도 mid분 동안 n명 이상의 심사를 할 수 있다면 반복문을 나간다.
            if people >= n:
                break
        
        # 심사 가능한 사람의 수가 심사 받아야할 사람의 수(n)보다 많거나 같은 경우, 즉 시간이 남는 경우
        if people >= n:
            answer = mid
            right = mid - 1
        # 심사 가능한 사람의 수가 심사 받아야할 사람의 수(n)보다 적은 경우, 즉 시간 내에 심사를 다 못할 경우
        elif people < n:
            left = mid + 1
            
    return answer

solution(6, [7, 10])