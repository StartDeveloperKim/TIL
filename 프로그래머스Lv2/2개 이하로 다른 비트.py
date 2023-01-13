## 알고리즘
## 1. 수를 이진수로 변환한다.(앞의 두개를 자르는 이유는 0b를 없애기 위함)
## 2. 처음 나오는 0을 1로 바꾸고 그 bit의 오른쪽 bit를 0으로 바꾼다.
## 3. 만약 내부 반복문에서 탈출하지 못했다면 for-else 문으로 인해 외부 else문으로 간다.
##    여기서는 맨 왼쪽 bit를 1로 바꾸고 그 오른쪽 bit를 0으로 바꾼다. 

def solution(numbers):
    answer=[]
    for number in numbers:
        reverseNum=reversed(list(bin(number))[2::])
        temp=1
        for n in reverseNum:
            if n=='0':
                number=number^temp
                number=number^(temp>>1)
                break
            temp=temp<<1
        else:
            number=number^temp # 맨 왼쪽 bit 반전
            number=number^(temp>>1) # 왼쪽에서 두번째 bit 반전
        answer.append(number)       
    return answer
