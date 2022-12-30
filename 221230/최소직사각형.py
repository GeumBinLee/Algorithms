def solution(sizes):
    for size in sizes :
        if size[1] > size[0] :
            size[0], size[1] = size[1], size[0]
    width = [x[0] for x in sizes]
    height = [x[1] for x in sizes]
    return max(width)*max(height)
