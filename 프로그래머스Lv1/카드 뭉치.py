## 문제풀이
## 1. idx1과 idx2는 각각 cards1과 cards2의 인덱스이다.
## 2. 해당 값들이 두 카드뭉치의 길이가 넘어가지 않고 맨 앞의 단어가 목표단어와 동일하다면
##    각 인덱스를 +1한ㄷ.
## 3. 둘다 다르다면 No를 반환한다.

def solution(cards1, cards2, goal):
    idx1, idx2 = 0, 0
    for g in goal:
        if idx1!=len(cards1) and g==cards1[idx1]:
            idx1+=1
        elif idx2!=len(cards2) and g==cards2[idx2]:
            idx2+=1
        else:
            break
    else:
        return "Yes"
