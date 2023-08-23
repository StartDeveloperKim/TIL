## 문제풀이
## 1. 각 숫자들을 모두 나눌 수 있는 수 중 가장 큰 수는 최대공약수를 의미한다.
## 2. reduce()"집계메서드"와 gcd()"최대공약수"를 이용하여 각 리스트의 최대공약수를 구한다.
## 3. 각 최대 공약수가 다른 리스트를 모두 나눌 수 있는지 체크한다.
## 4. 둘 최대 공약수 모두 해당된다면 둘 중 최대값을 반환한다.
## 5. 둘 다 해당되지 않는다면 0을 반환한다.

from math import gcd
from functools import reduce

def solution(arrayA, arrayB):
    answer = []
    aGcd, bGcd = reduce(gcd, arrayA), reduce(gcd, arrayB)
    for a in arrayA:
        if a%bGcd==0:
            break
    else:
        answer.append(bGcd)

    for b in arrayB:
        if b%aGcd==0:
            break
    else:
        answer.append(aGcd)
    return max(answer) if len(answer)>0 else 0
