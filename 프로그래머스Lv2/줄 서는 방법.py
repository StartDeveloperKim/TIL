## 생각1:
##     처음에는 permutations를 이용했는데 효율성에서 걸렸다.
## 생각2:
##     오름차순으로 정렬했을 때 각 자리마다 순서를 지정할 수 있다고 생각했다.
##     1. (k/(n-1)!)의 결과를 올림연산을 하고 1을 빼서 남은 수의 인덱스로 활용하면
##        그 다음 순번의 수를 알 수 있다.
##     2. 그러면 총 n번 반복으로 정답을 구할 수 있다.

from math import factorial
from math import ceil

answer = []

def calculator(n, k, number):
    global answer
    
    if len(number)==0:
        return
    answer.append(number.pop(ceil(k/factorial(n-1))-1))
    calculator(n-1, k%factorial(n-1), number)

def solution(n, k):
    calculator(n, k, list(range(1, n+1)))
    
    return answer
