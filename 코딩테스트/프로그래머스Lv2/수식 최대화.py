## 알고리즘
## 1. 문자열에서 숫자와 연산자를 각각 분리
## 2. 순열을 통해 수식이 가지고 있는 연산자 우선순위 순열 구하기
## 3. 우선순위 1, 2번째 연산자까지 수식 계산하고 리스트 갱신
## 4. 마지막에 우선순위가 제일 낮은 연산자만 남은 수식을 계산
## 5. 계산된 값 중 최댓값을 정답으로 함

from itertools import permutations

def solution(expression):
    answer = -1
    numbers, operators=[], list(set([o for o in expression if o.isdigit()==False]))
    num=''
    for e in expression:
        if e.isdigit():
            num+=e
        else:
            numbers.append(num)
            numbers.append(e)
            num=''
    numbers.append(num)
    
    for permutation in list(permutations(operators, len(operators))):
        numbersCopy=numbers.copy()
        for i in range(len(permutation)-1):
            result, idx=[], 0
            length=len(numbersCopy)
            while idx<length:
                if numbersCopy[idx]==permutation[i]:
                    result.append(str(eval(result.pop()+numbersCopy[idx]+numbersCopy[idx+1])))
                    idx+=2
                else:
                    result.append(numbersCopy[idx])
                    idx+=1
            numbersCopy=result.copy()
        
        answer=max(answer, abs(eval(''.join(numbersCopy)))) 
        
    return answer



