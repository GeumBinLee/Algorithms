def solution(absolutes, signs):
    numbers = ["0" for _ in range(len(absolutes))]
    for n in range(len(absolutes)) :
        if str(signs[n]) == "True" :
            numbers[n] = str(absolutes[n])
        else :
            numbers[n] = "-"+str(absolutes[n])
    answer = list(map(int, numbers))
    return sum(answer)

print(solution([4,7,12],[True,False,True]))