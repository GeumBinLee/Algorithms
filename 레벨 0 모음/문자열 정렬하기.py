def solution(my_string):
    return sorted([int(x) for x in my_string if x.isdigit()])

# 다른 사람 풀이 -> 정규표현식 활용
# 으악 정규표현식은 아직 생소해
import re

def solution(my_string):
    return sorted(map(int, (list(re.sub('[^0-9]', '', my_string)))))

# 다른 풀이2 -> filter랑 map 활용
# 굳이 filter에 lambda까지 쓸 필요가 있었을까 싶긴 함 효율도 큰 차이 안 나는 거 같은데
def solution(my_string):
    return sorted(map(int, filter(lambda s: s.isdigit(), my_string)))
