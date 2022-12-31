# def solution(s):
#     for _ in range(len(s)) :
#         s = s.replace("()","")
#     if len(s) == 0 :
#         return True
#     return False
# 효율성 검사 통과 안 됨..

def solution(s):
    count = 0
    for b in s :
        if b == '(' :
            count +=1
        else :
            count -= 1
        if count < 0 :
            return False
    if count == 0 :
        return True
    return False
    
    
s = "()())"
solution(s)