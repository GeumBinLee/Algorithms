def solution(arr):
    answer = []
    answer.append(arr[0]) # 첫 번째 값 넣어주기
    for k in range(1, len(arr)) :
        if arr[k-1] != arr[k] : # 이전 값이랑 다르다면
            answer.append(arr[k])
    return answer