def solution(order):
    return sum([1 for x in str(order) if int(x) in [3, 6, 9]])

# 다른 풀이
def solution(order):
    return sum(map(lambda x: str(order).count(str(x)), [3, 6, 9]))