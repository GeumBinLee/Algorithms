# def solution(n, lost, reserve) :
#     temp = [1 for _ in range(n+2)]
#     temp[0] = 0
#     temp[-1] = 0
    
#     for lo in lost :
#         temp[lo] = 0
    
#     for re in reserve :
#         if temp[re] == 0:
#             temp[re] = 1
#             continue
#         temp[re] = 2
    
#     for i in range(1 ,n+1) :
#         if temp[i] == 0 :
#             if temp[i -1] == 2 :
#                 temp[i-1] -= 1
#                 temp[i] = 1
#             elif temp[i+1] == 2 :
#                 temp[i+1] -= 1
#                 temp[i] = 1
                
#     return sum([1 for x in temp if x != 0])

arr = [5, 8, 1, 2, 4, 9, 3, 7, 6]
print("sorted data :", sorted(arr))
print("input data: ", arr)
arr.sort()
print("input data: ", arr)

arr2 = [("smith", 95), ("John", 78), ("Paul", 87), ("Jack", 61), ("Ryan", 97)]
res = sorted(arr, key = lambda x : x[1])
print(res)