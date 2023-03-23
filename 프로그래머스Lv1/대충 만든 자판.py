def solution(keymap, targets):
    answer = []
    num=101
    alpha={'A':num, 'B':num, 'C':num, 'D':num, 'E':num, 'F':num,
          'G':num, 'H':num, 'I':num, 'J':num, 'K':num, 'L':num, 
          'M':num, 'N':num, 'O':num, 'P':num, 'Q':num, 'R':num,
          'S':num, 'T':num, 'U':num, 'V':num, 'W':num, 'X':num, 'Y':num, 'Z':num}
    for key in keymap:
        for i, k in enumerate(key):
            alpha[k]=min(alpha[k], i+1)
    
    for target in targets:
        cnt=0
        for t in target:
            if alpha[t]==num:
                cnt=-1
                break
            cnt+=alpha[t]
        answer.append(cnt)
    return answer
