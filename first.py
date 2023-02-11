# lotteries = 2차원 배열
# [당첨자 수, 구매한 사람 수, 당첨 금액]
# 확률 = 당첨자 수/(구매한 사람 수 + 1)
def solution(lotteries):
    answer = 0
    turn = 0
    money = 0
    probability = 0
    lot = []
    
    for lottery in lotteries :
        turn += 1
        next_probability = lottery[0]/(lottery[1]+1)
        
        if lottery[0] >= lottery[1] +1 :
            lot.append((turn, lottery[2]))
    if lot :
        lot.sort(key = lambda x : x[1], reverse=True)
        print(lot[0][0])
        return lot[0][0]
    else :
        turn = 0
        
        
    for lottery in lotteries :
        
        turn += 1
        next_probability = lottery[0]/(lottery[1]+1)
        
        if lottery[0] >= lottery[1]+1 :
            probability = 100
            money = lottery[2]
            answer = turn
        
        elif next_probability > probability :
            probability = next_probability
            money = lottery[2]
            answer = turn
            
        elif next_probability == probability :
            if lottery[2] > money :
                probability = next_probability
                money = lottery[2]
                answer = turn
        
    return answer

solution([[100,100,500],[1000,1000,100]])