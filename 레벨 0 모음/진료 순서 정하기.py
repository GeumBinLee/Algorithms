def solution(emergency):
    sorted_emergency = sorted(emergency, reverse=True)
    for i in range(len(emergency)):
        emergency[i] = sorted_emergency.index(emergency[i]) +1
    return emergency

# 다른 사람 풀이 -> 같은 풀이인데 축약식으로 품
def solution2(emergency):
    return [sorted(emergency, reverse=True).index(e) + 1 for e in emergency]
