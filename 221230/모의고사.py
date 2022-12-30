def solution(answers):
    answer = []
    count = [0,0,0]
    arr1 = [1,2,3,4,5]
    arr2 = [2,1,2,3,2,4,2,5]
    arr3 = [3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)) :
        if answers[i] == arr1[i%5] :
            count[0] += 1
        if answers[i] == arr2[i%len(arr2)] :
            count[1] += 1
        if answers[i] == arr3[i%len(arr3)] :
            count[2] += 1
    max_count = max(count)
    return [i+1 for i, x in enumerate(count) if x == max_count]