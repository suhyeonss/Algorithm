def solution(s, skip, index):
    answer = ''
    whole = [chr(i) for i in range(97,123) if chr(i) not in skip]
    for word in s:
        l = whole.index(word)+index
        if l >= len(whole):
            l = l%len(whole)
        answer += whole[l]
    return answer