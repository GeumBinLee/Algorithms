# def solution(s):
#     while 1 :
#         if s.count("()") == 0 :
#             break
#         s =s.replace("()", "")
#     if len(s) == 0 :
#         return True
#     return False
# 실행시간 초과

# def solution(s):
#     for _ in range(len(s)) :
#         s = s.replace("()","")
#     if len(s) == 0 :
#         return True
#     return False
# 효율성 검사 통과 안 됨..

# def solution(s):
#     for _ in range(len(s)) :
#         if "()" in s :
#             s = s.replace("()","")
#         else :
#             break
#     if len(s) == 0 :
#         return True
#     return False
# 효율성 검사 통과 안 됨...