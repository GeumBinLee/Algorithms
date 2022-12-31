# 스타상 x2(현재랑 바로 직전 거), 아차상 -기호와 같다.
# single 1제곱, double 2제곱, triple 3제곱
# 끊기만 잘 끊고 S, D, T 먼저 적용 후에 *, # 적용

def solution(dartResult):
    dart_list = list(dartResult)
    only_pair = [x for x in dart_list if x != "*" and x !='#']
    only_num = ""
    bonus = []
    
    # 점수랑 S, D, T 구분하기
    for num in only_pair :
        try :
            if int(num) :
                only_num += num
            if num == "0" :
                only_num += "0"
        except ValueError :
            only_num += ','
            bonus.append(num)
    only_num = only_num.split(',')[:-1]
    
    for i in range(len(bonus)) :
        if bonus[i] == 'S' :
            bonus[i] = "*1"
        elif bonus[i] == 'D' :
            bonus[i] = "**2"
        elif bonus[i] == 'T':
            bonus[i] = "**3"
            
    # '*' 인덱스 구하기
    star_index = []
    while '*' in dart_list :
        star_index.append(dart_list.index('*'))
        dart_list.pop(dart_list.index('*'))
        
    # '#' 인덱스 구하기
    hash_index = []
    while '#' in dart_list :
        hash_index.append(dart_list.index('#'))
        dart_list.pop(dart_list.index('#'))
        
    # 숫자 + S / D / T 결과만 구하기    
    score = [0,0,0]
    for i in range(3) :
        score[i] = eval(f"{only_num[i]}{bonus[i]}")
    
    for star in star_index :
        if int(star) > 5 :
            score[2] *= 2
            score[1] *= 2
        elif int(star) > 3 :
            score[1] *= 2
            score[0] *= 2
        else :
            score[0] *= 2
    
    for hash_ in hash_index :
        if int(hash_) > 5 :
            score[2] *= -1
        elif int(hash_) > 3 :
            score[1] *= -1
        else :
            score[0] *= -1
    return sum(score)
            
    
solution("1T2D3D#")
# solution("1S1S1D")