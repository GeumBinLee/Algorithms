# 내 풀이 1
def solution(hp):
    answer = 0
    while hp :
        answer += 1
        if hp >= 5 :
            hp -= 5
        elif hp >= 3 :
            hp -= 3
        else :
            hp -= 1
    return answer

# 다른 풀이 -> 깔끔쓰
def solution(hp):    
    return hp // 5 + (hp % 5 // 3) + ((hp % 5) % 3)

# 다른 풀이 2 -> divmod(x, y)
# divmod(num1,num2) # num1을 num2 로 나눈 몫과 나머지를 출력하는 함수
def solution(hp):
    answer = 0
    for ant in [5, 3, 1]:
        d, hp = divmod(hp, ant)
        answer += d
    return answer