## 완전탐색 문제이다.
## 순열 라이브러리를 활용하여 주어진 numbers안의 숫자들로 만들 수 있는 모든 숫자의 조합을 만들었다.
## 그후 그 숫자들의 소수 여부를 체크했다.
## 꿀팁 : 소수를 체크할 때의 나머지 연산 구간을 2부터 주어진 숫자의 0.5제곱 +1 까지만해도 검증이 가능하다.

from itertools import permutations

def check_prime(number):
    if number==0 or number==1:
        return False
    elif number==2:
        return True
    
    for num in range(2, int(number**0.5)+1):
        if number%num==0:
            return False
    return True

def solution(numbers):
    answer = 0
    temp=[]
    for i in range(1, len(numbers)+1):
        for number in permutations(list(numbers), i):
            temp.append(int(''.join(list(number))))
    make_numbers=list(set(temp))
    
    for number in make_numbers:
        if check_prime(number):
            answer+=1
    
    return answer
