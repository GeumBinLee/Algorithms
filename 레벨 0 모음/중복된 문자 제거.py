def solution2(my_string):
    answer = ""
    for string in my_string :
        if string not in answer :
            answer += string
    return answer

# 다른 풀이
def solution(my_string):
    return ''.join(dict.fromkeys(my_string))