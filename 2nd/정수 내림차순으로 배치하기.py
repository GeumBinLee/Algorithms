def solution(n):
    num = []
    for i in str(n) :
        num.append(i)
    num.sort(reverse=True)
    answer = ""
    for k in num :
        answer += k
    return int(answer)

print(solution(118372))