from itertools import permutations

def is_prime_number(num):
    if num==0 or num==1:
        return False
    else:
        for n in range(2, (num//2)+1):
            if num % n == 0:
                return False        
        return True

# def solution(numbers):
#     number_list = list(map(int, numbers))
#     number_list.sort(reverse=True)
    
    # max_num = ""
    # for x in number_list :
    #     max_num += str(x)
    
#     prime_numbers = []
#     for i in range(2, int(max_num)+1) :
#         if is_prime_number(i) :
#             prime_numbers.append(i)
    
#     permute_list = ()
#     for i in range(1, len(max_num)+1) :
#         permute = list(permutations(number_list, i))
            
#         for p in permute :
#             permute_list += p
            
#     s1 = set(prime_numbers)
    
    # 중도 포기
    
def solution(numbers) :
    # 종이에 적힌 숫자 떼어내기
    number_list = list(map(int, numbers))
    number_list.sort(reverse=True)
    
    # 숫자 조합 중 가장 큰 수 구하기
    max_num = ""
    for x in number_list :
        max_num += str(x)
    
    # 한자릿수 조합부터 가장 큰 수와 동일한 자릿수까지 모든 조합 구하기
    permute_list = []
    for i in range(1, len(max_num)+1) :
        permute = list(permutations(number_list, i))
        permute_list += permute
        
    # 조합 중 소수에 해당하는 조합만 골라내기
    permute_numbers = []
    for pl in permute_list :
        permute_number = ""
        for p in pl :
            permute_number += str(p)
        permute_numbers.append(int(permute_number))
    
    # 중복값 없애고 해당 set 안 요소의 개수 반환
    prime_set = []
    for i in permute_numbers :
        if is_prime_number(i) :
            prime_set.append(i)
    prime_set = set(prime_set)
    
    return len(prime_set)
    
solution("011")

