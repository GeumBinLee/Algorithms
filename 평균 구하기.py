def solution(arr):
    answer = 0
    answer = sum(arr) / len(arr)
    return answer

# 평균이니까 총합을 총 개수로 나누면 되는데 총합은 sum으로 쉽게 구할 수 있고
# 총 개수는 lend으로 쉽게 구할 수 있으니까 sum함수의 결과를 len함수의 결과로 나누자고 생각