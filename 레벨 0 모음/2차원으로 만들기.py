def solution(num_list, n):
    answer = []
    length = len(num_list)
    for i in range(length//n) :
        answer.insert(i, num_list[:n])
        del num_list[:n]
    return answer

# 다른 사람 풀이
def solution(num_list, n):
    answer = []
    length = len(num_list)
    for i in range(length//n) :
        answer.insert(i, num_list[:n])
        del num_list[:n]
    return answer

# 다른 풀이 2
def solution(num_list, n):
    return [num_list[ix-n:ix] for ix in range(n, len(num_list)+1, n)]

solution([1, 2, 3, 4, 5, 6, 7, 8], 2)