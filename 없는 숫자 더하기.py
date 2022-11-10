url = "https://school.programmers.co.kr/learn/courses/30/lessons/86051"

# 어차피 numbers가 숫자가 겹칠 일 없기도 하고, set이 차집합 구하기 쉬우니까 미리 0부터 9까지 들어가있는 set 데이터를 만들고 거기서 차집합 하고 남은 애들을 sum함수로 더해주면 될 거 같다
# 0부터 9까지가 담긴 set을 for문으로 만들어도 괜창을 거 같은데 숫자가 많은 게 아니라 그냥 만들어야겠다.


def solution(numbers):
    every_number = {0,1,2,3,4,5,6,7,8,9}
    every_number -= set(numbers)
    answer = sum(every_number)
    return answer