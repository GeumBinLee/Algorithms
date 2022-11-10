def solution(num):
    answer = ''
    if num%2 == 0 :
        answer = "Even"
    else :
        answer = "Odd"
    return answer
    
# 짝수는 2로 나눈 나머지가 0이고 홀수는 2로 나눈 나머지가 1이니까 나머지가 0이면 Even을 반환하고 1이면 Odd를 반환하게 하자
# num이 0이어도 짝수로 친다니까 따로 0인 경우는 처리해주지 않아도 되겠다.