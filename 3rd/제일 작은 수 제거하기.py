# def solution(arr):
#     minimum = min(arr)
#     indexing = arr.index(minimum)
#     arr.pop(indexing)
#     if len(arr) == 0 :
#         arr.append(-1)
#     return arr

def solution(arr) :
    if len(arr) > 1 :
        arr.remove(min(arr))
        return arr
    else :
        return [-1]