def solution(my_string):
    answer = 0
    for string in my_string :
        try :
            answer += int(string)
        except :
            pass
    return answer

# 다른 풀이 -> .isdigit() 활용
def solution(my_string):
    return sum(int(i) for i in my_string if i.isdigit())