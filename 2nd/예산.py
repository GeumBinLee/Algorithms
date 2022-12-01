def solution(d, budget):
    d.sort()
    receive = []
    if sum(d) <= budget :
        return len(d)
    else :
        for n in range(len(d)) :
            receive.append(d[n])
            if sum(receive) > budget :
                break
        return len(receive)-1

print(solution([2,2,3,3], 10))