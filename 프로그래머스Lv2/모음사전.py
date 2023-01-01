from itertools import combinations

def solution(word):
    answer = 0
    words=[]
    for i in range(1, 6):
        vowel=['A', 'E', 'I', 'O', 'U']*i
        for p in list(combinations(vowel, i)):
            words.append(''.join(p))

    dictionary=list(set(words))
    dictionary.sort()

    return dictionary.index(word)+1
