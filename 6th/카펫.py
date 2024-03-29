def solution(brown, yellow) :
    n = (brown - 4) // 2
    
    for i in range(1, n) :
        x, y = i, n - i
        if x * y == yellow :
            return [y + 2, x + 2]
solution(10, 2)

def solution2(brown, yellow) :
    n = (brown-4)//2
    start = 1; end = int(n**1/2)+1
    while start <= end :
        mid = (start+end)//2
        target = mid * (n-mid)
        if target == yellow :
            return [n-mid+2, mid+2]
        elif target > yellow :
            end = mid-1
        else :
            start = mid+1