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
    
# 다른 풀이
def solution(s) :
    stack = []
    for c in s :
        if c == "(" :
            stack.append(c)
        else : # ) 라면
            if stack != [] : # 쌍이 있다면
                stack.pop()
            else :
                return False
    if stack != [] :
        return False
    return True