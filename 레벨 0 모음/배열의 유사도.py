# 내 풀이
def solution(s1, s2):
    return sum([1 for x in s1 if x in s2])

#다른 풀이 -> set 자료형 교집합 활용
def solution(s1, s2):
    return len(set(s1)&set(s2))

# 다른 풀이 -> 마찬가지로 set 자료형 교집합 활용
# return에 한 줄로 싹 적어도 될듯
def solution(s1, s2):
    s1 = set(s1)
    s2 = set(s2)
    return len(s1.intersection(s2))