def solution(numbers):
    every_number = {0,1,2,3,4,5,6,7,8,9}
    every_number -= set(numbers)
    answer = sum(every_number)
    return answer