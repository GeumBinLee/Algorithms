def solution(N, stages):
    answer = []
    
    # 스테이지에 도달한 플레이어의 수 구하기
    reach = [0 for _ in range(N)]
    for stage in stages:
        if stage > N:
            for k in range(len(reach)):
                reach[k] += 1
        else:
            for n in range(stage):
                reach[n] += 1
    print(f"reach = {reach}")

    # 클리어하지 못한 사람의 수 구하기
    not_clear = [0 for _ in range(N)]
    for i in range(1, N+1):
        not_clear[i-1] = stages.count(i)
    print(f"클리어 ㄴㄴ ={not_clear}")

    # 실패율 구하기 : 아직 클리어하지 못한 사람 수 / 스테이지에 도달한 플레이어 수
    fail = {}
    for a in range(N) :
        if not_clear[a] == 0 :
            fail[eval(f"{a}+1")] = 0
        else :
            per = not_clear[a]/reach[a]
            fail[eval(f"{a}+1")] = per
            
    before_answer = sorted(fail.items(), reverse=True, key=lambda x : x[1])
    for an in before_answer :
        answer.append(an[0])
    return answer
        
        
    

solution(5, [2, 1, 2, 6, 2, 4, 3, 3])