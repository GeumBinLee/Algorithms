# 내 풀이
def solution(my_string):
    vowel = ['a', 'e', 'i', 'o', 'u']
    for v in vowel :
        my_string = my_string.replace(v, "")
    return my_string

# 다른 풀이 -> join 사용
def solution(my_string):
    return "".join([i for i in my_string if not(i in "aeiou")])
# "".join([i for i in my_string if i not in "aeiou"])가 더 보기 좋은듯