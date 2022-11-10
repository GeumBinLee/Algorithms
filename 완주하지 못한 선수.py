# 시험 삼아 .remove 해보니까 한개씩만 없어지길래 remove로 없애기로 했당
# 어차피 무조건 결과가 한 사람이라서 마지막에 리스트의 0번째 인덱스로 뽑으면 될 듯?

def solution(participant, completion):
    answer = ''
    for person in completion :
        participant.remove(person)
    answer = participant[0]
    return answer