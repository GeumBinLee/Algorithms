def solution(n, arr1, arr2):
    answer = []
    
    binary_arr1 = []
    binary_arr2 = []
    
    for i in range(n) :
        binary_arr1.append(bin(arr1[i])[2:].zfill(n))
        binary_arr2.append(bin(arr2[i])[2:].zfill(n))

    for k in range(n) :
        wall = ""
        for w in range(n) :
            if binary_arr1[k][w] == "0" and binary_arr2[k][w] == "0" :
                wall += " "
            else : 
                wall += "#"
        answer.append(wall)
    print(answer)
    return answer