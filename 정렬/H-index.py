def solution(citations): 
    citations.sort(reverse=True)
    count = 0
    indexing = 0
    for i in range(len(citations)) :
        if citations[i] <= i :
            indexing = i
            break
    for citation in citations :
        if citation > indexing :
            count += 1
    return count
    
solution([3,0,6,1,5])

# 다른 풀이
def solution(citations) :
    citations.sort(reverse=True)
    for idx, citation in enumerate(citations) :
        if idx >= citation :
            return idx
    return len(citations)