def solution(N, stages):
    answer = []
    
    # 스테이지에 도달한 플레이어의 수 구하기
    reach = [0 for _ in range(N)]
    for stage in stages:
        if stage > N: # 머무르는 스테이지가 총 스테이지보다 높다면
            for k in range(N):
                reach[k] += 1 # 모든 스테이지에 대해 도달한 사람 한 명씩 추가
        else: # 머무르는 스테이지가 최고 스테이지보다 아래, 즉 하다가 막혔다면
            for n in range(stage): # 도달한 층까지만 사람 한명씩 추가
                reach[n] += 1
    print(f"reach = {reach}")

    # 클리어하지 못한 사람의 수 구하기
    not_clear = [0 for _ in range(N)]
    for i in range(1, N+1): # 현재 있는 위치가 1보다 작거나 총스테이지수보다 높으면 셀 필요가 없음.
        not_clear[i-1] = stages.count(i) # n층 스테이지에 머물러있다는 건 n층을 통과하지 못했다는 말이므로 n층에 머물러있는 사람의 수(=n의 개수)를 카운트해서 넣는다.
    print(f"클리어 ㄴㄴ ={not_clear}")

    # 실패율 구하기 : 아직 클리어하지 못한 사람 수 / 스테이지에 도달한 플레이어 수
    fail = {} # {"층수" : 실패율} pair 만들기 위함
    for a in range(N) :
        if not_clear[a] == 0 : # zerodivision 어쩌구 에러 안 나게 클리어하지 못 한 사람이 없을 경우 처리
            fail[eval(f"{a}+1")] = 0 # 인덱스랑 스테이지는 1씩 차이 나니까 a(인덱스)+1층의 실패율 0으로 세팅
        else :
            per = not_clear[a]/reach[a] # value값에 해당하는 실패율 구하기
            fail[eval(f"{a}+1")] = per # a(인덱스)+1이 스테이지니까 해당 스테이지에 실패율 값 매칭
            
    before_answer = sorted(fail.items(), reverse=True, key=lambda x : x[1]) # value에 해당하는 실패율 기준으로 내림차순 정렬
    print(before_answer)
    for an in before_answer : # 튜플에서 스테이지에 해당하는 첫 번째 인자만 뽑아내기
        answer.append(an[0])
    return answer
        
        
    

solution(5, [2, 1, 2, 6, 2, 4, 3, 3])