def solution(arr):
    minimum = min(arr)
    indexing = arr.index(minimum)
    arr.pop(indexing)
    if len(arr) == 0 :
        arr.append(-1)
    return arr

solution([4,3,2,1])