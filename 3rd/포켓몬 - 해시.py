# 총 포켓몬 수 = len(nums)
# 가져갈 포켓몬 수 = len(nums)//2

def solution(nums):
    take = len(nums)//2
    if take >= len(set(nums)) :
        return len(set(nums))
    return take