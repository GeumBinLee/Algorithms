def solution(sizes):
    for size in sizes :
        if size[1] > size[0] :
            size[0], size[1] = size[1], size[0]
    width = [x[0] for x in sizes]
    height = [x[1] for x in sizes]
    return max(width)*max(height)

# 다른 풀이
def solution2(sizes) :
    width = 0
    height = 0
    
    for i in range(len(sizes)) :
        sizes[i].sort()
        width = max(width, sizes[i][0])
        height = max(height, sizes[i][1])
    
    answer = width * height
    return answer