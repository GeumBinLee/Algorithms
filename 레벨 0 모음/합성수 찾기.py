def solution(n):
    
    if n < 4:
        return 0
    
    answer = 0
    for i in range(4, n+1) :
        count = 0
        for a in range(1, i+1) :
            if i % a == 0 :
                count += 1
        
        if count >= 3 :
            answer += 1
            
    print(answer)
    return answer

solution(10)


# 다른 풀이 1

def solution1(n):
    output = 0
    for i in range(4, n + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                output += 1
                break
    return output

# 다른 풀이 2
def get_divisors(n):
    return list(filter(lambda v: n % v ==0, range(1, n+1)))

def solution(n):
    return len(list(filter(lambda v: len(get_divisors(v)) >= 3, range(1, n+1))))

# 다른 풀이 3
def solution(n):
    return len([i for i in range(2, n + 1) if not all(i % j for j in range(2, i))])