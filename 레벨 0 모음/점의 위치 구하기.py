# 내 풀이
def solution(dot):
    answer = 0
    if dot[0] > 0 :
        if dot[1] > 0 :
            return 1
        else :
            return 4
    else :
        if dot[1] > 0 :
            return 2
        else :
            return 3
    return answer

# 다른 풀이
def solution(dot):
    quad = [(3,2),(4,1)]
    return quad[dot[0] > 0][dot[1] > 0]

# 다른 풀이 2 -> 사실상 위랑 같은 풀이
def solution(dot):
    return [[1, 4], [2, 3]][dot[0] < 0][dot[1] < 0]

# 다른 풀이 3
def solution(dot):
    a, b = 1, 0
    if dot[0]*dot[1] > 0:
        b = 1
    if dot[1] < 0:
        a = 2
    return 2*a-b