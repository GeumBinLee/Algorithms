def solution(num):
    answer = 0
    if num == 1 :
        return 0
    while 1 :
        # 사실상 콜라츠 추측을 코드로 옮겼을 뿐
        if num%2 == 0 :
            num /= 2
            answer += 1
        else :
            num = num*3 + 1
            answer += 1
         
        # 500 되는 순간 return -1   
        if answer >=500 :
            return -1
        
        # num이 1이 되는 순간 카운팅 횟수 반환
        if num == 1 :
            return answer

# 어차피 절차상 else문이 없어도 알아서 걸러서 할 거 같아서 복잡하게 쓰기보단 간단하게 쓰려고 이렇게 작성했는데 괜찮..? 은지는...? 잘...? 모르겠습니다.