def solution(age):
    answer = ''
    for s in str(age) :
        answer += chr(int(s)+97)
    return answer

# 다른 풀이

2
3
4
def solution(age):

    return ''.join([chr(int(i)+97) for i in str(age)])
