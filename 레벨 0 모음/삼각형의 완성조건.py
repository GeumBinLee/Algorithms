# 내 풀이
def solution(sides):
    maxi = max(sides)
    rest = sum(sides) - maxi
    if maxi >= rest :
        return 2
    return 1

# 다른 풀이
def solution(sides):
    sides.sort()
    return 1 if sides[0]+sides[1]>sides[2] else 2