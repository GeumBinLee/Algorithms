# 내 풀이
def solution(rsp) :
    answer = ""
    for r in rsp :
        if r == "2" :
            answer += "0"
        elif r == "5" :
            answer += "2"
        else :
            answer += "5"
    return answer

# 다른 풀이 -> join 활용
# 내가 join 쓸 생각을 잘 못한느듯
def solution(rsp):
    d = {'0':'5','2':'0','5':'2'}
    return ''.join(d[i] for i in rsp)

# 다른 풀이 2
def solution(rsp):
    rsp =rsp.replace('2','s')
    rsp =rsp.replace('5','p')
    rsp =rsp.replace('0','r')
    rsp =rsp.replace('r','5')
    rsp =rsp.replace('s','0')
    rsp =rsp.replace('p','2')
    return rsp