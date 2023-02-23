morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
}

def solution(letter):
    new_letter = letter.split(' ')
    answer = ""
    for new in new_letter :
        answer += morse[new]
    return answer

# 다른 풀이

def solution(letter):
    return ''.join([morse[i] for i in letter.split(' ')])

    
solution(".... . .-.. .-.. ---")