# 내 풀이
# 다른 풀이 보고 나니 굳이 reduce()를 쓸 필욘 없었을 거 같음
from functools import reduce

def solution(n):
    return reduce(lambda x, y : x + y, [int(d) for d in str(n)], 0)

# 다른 풀이
# str(n)은 굳이 list() 사용 안 해도 됐었을 듯
def solution(n):
    answer = sum(list(map(int,list(str(n)))))
    return answer