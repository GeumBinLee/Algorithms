def solution(before, after):
    for b in before :
        if before.count(b) != after.count(b) :
            return 0
    return 1

# 다른 풀이
def solution(before, after):
    return 1 if sorted(before)==sorted(after) else 0