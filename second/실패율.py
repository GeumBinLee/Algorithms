from collections import Counter

def solution(N, stages):
    # 스테이지에 도달한 플레이어의 수 구하기
    reach = [0 for _ in range(N)]
    for stage in stages :
        if stage > N :
            for k in range(len(reach)) :
                reach[k] += 1
        else : 
            for n in range(stage) :
                reach[n] += 1
    print(f"reach = {reach}")
    
    # 클리어하지 못한 사람의 수 구하기
    not_clear = dict(Counter(stages))
    print(not_clear)
    not_clear_list = [0 for _ in range(N)]
    print(not_clear_list)
    print(not_clear.keys())
    for i in range(N) :
        if not_clear[i+1]:
            not_clear_list[i] = not_clear[i+1]
        else :
            not_clear_list[i] = 0
    print(not_clear_list)
    
    # 실패율 구하기 : 아직 클리어하지 못한 사람 수 / 스테이지에 도달한 플레이어 수
    fail = {}
    for a in range(N) :
        if not_clear[a] == 0 :
            fail[eval(f"{a}+1")] = 0
        else :
            per = not_clear[a]/reach[a]
            fail[eval(f"{a}+1")] = per
            
    answer = dict(sorted(fail.items()))
    print(answer)
    
    return answer

solution(5, [2, 1, 2, 6, 2, 4, 3, 3])