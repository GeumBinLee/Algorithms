def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    start, end = 0, distance
    
    while start <= end: 
        mid = (start + end) // 2
        del_rock = 0 # 제거 횟수 카운트
        stone = 0 # 기준점
        for rock in rocks:
            if rock - stone <  mid: # 거리가 mid보다 작으면 제거한다.
                del_rock += 1 
            else: # 돌 사이 거리가 mid보다 크면 기준을 바꾼다.
                stone = rock
             
            if del_rock > n: #제거된 돌이 문제 조건 보다 크면 for문을 나온다
                break
        
        if del_rock > n: # 제거할 바위 수(n)보다 많은 바위를 제거했을 시 범위를 줄인다.
            end = mid - 1
        else: # 그게 아니면 큰 쪽으로 줄인다.
            answer = mid
            start = mid + 1
        print(f"start : {start}, end : {end}, mid : {mid}, del_rock : {del_rock}, answer :{answer}")
            
    return answer

solution(25, [2, 14, 11, 21, 17], 2)