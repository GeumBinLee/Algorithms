def solution(s):
    answer = 0
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    numbers_dict = {}
    
    for k, i in enumerate(numbers) :
        numbers_dict[i] = str(k)
    
    for num in numbers :
        if num in s :
            new = s.replace(num, numbers_dict[num])
            s=new
    answer = int(s)
    return answer