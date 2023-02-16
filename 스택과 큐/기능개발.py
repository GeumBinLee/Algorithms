def solution1(progresses, speeds):
    answer = [0]
    days = []

    # 각 기능별 소요일 구하기
    for i in range(len(progresses)) :
        if (100-progresses[i]) % speeds[i] == 0 :
            days.append((100-progresses[i])//speeds[i])
        else :
            days.append((100-progresses[i])//speeds[i] + 1)

    start = days[0]
    for day in days :
        if day <= start :
            answer[-1] += 1
        else :
            answer.append(1)       
    
    return answer


def solution(progresses, speeds) :
    answer = []
    
    while progresses :
        count = 0
        
        progresses = [progresses[i] + speeds[i] for i in range(len(progresses))]
        
        while progresses and progresses[0] >= 100 :
            count += 1
            progresses.pop(0)
            speeds.pop(0)
        
        if count > 0 : 
            answer.append(count)
    
    return answer

solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])
# 5 10 1 1 20 1 # 1, 3, 2
# solution([93, 30, 55], [1, 30, 5])
# 7 3 9 # 2 1