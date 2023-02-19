# 내 풀이
def solution(cipher, code):
    return "".join(cipher[i] for i in range(code-1, len(cipher), code))

# 다른 풀이 -> 슬라이싱 활용
def solution(cipher, code):
    return cipher[code-1::code]