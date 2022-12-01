from itertools import combinations

def is_prime_number(num):
    if num==0 or num==1:
        return False
    else:
        for n in range(2, num-1):
            if num % n == 0:
                return False        
        return True

def solution(nums):
    sum_nums = [sum(x)for x in combinations(nums,3)]
    count = 0
    for num in sum_nums :
        if is_prime_number(num) :
            count += 1
    return count
    
solution([1,2,3,4])