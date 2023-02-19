# 내 풀이
def solution(numbers, direction):
    if direction == "right" :
        numbers.insert(0, numbers[-1])
        del numbers[-1]
    else :
        numbers.append(numbers[0])
        del numbers[0]
    return numbers

# 다른 풀이
def solution(numbers, direction):
    return [numbers[-1]] + numbers[:-1] if direction == 'right' else numbers[1:] + [numbers[0]]