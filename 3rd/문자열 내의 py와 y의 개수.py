def solution(s):
    lower_s = s.lower()
    if lower_s.count("y") != lower_s.count("p") :
        return False
    return True