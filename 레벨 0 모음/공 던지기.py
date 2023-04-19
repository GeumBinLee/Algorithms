def solution(numbers, k):
    turn = (1 + 2 * (k-1))%len(numbers)
    return numbers[turn-1]