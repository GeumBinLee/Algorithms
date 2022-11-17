def solution(left, right):
    answer = 0
    
    for num in range(left, right+1) :
        list_ = []
        for k in range(1, num) :
            if num % k == 0 :
                list_.append(k)
        if len(list_)%2 == 0 :
            answer += num
        else :
            answer -= num
    return answer