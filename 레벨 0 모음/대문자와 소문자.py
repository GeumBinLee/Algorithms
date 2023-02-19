# 내 풀이
def solution(my_string):
    return "".join(string.upper() if string.islower() else string.lower() for string in my_string)

# 다른 풀이 -> swap() 활용
# 방금 푼 문제에서 join 보고 바로 써서 뿌듯했는데 이게 머꼬...
# swapcase()는 대소문자를 변환해준다.
def solution(my_string):
    return my_string.swapcase()