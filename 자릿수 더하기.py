def solution(n):
    answer = 0
    for i in str(n) :
        answer += int(i)
    return answer

# 자릿수를 더한다는 건 결국 각 숫자들을 각기 다른 개체로 본다는 거니까 걍 다 따로 떼와서 더하면 되겠다.
# 따로 떼오는 동작이 반복적이니까 for문을 돌리자. 이때 int는 인덱싱이 안 되니까 str으로 진행