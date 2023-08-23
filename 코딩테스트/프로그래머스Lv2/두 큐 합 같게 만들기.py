## *시간초과문제 해결:
##     sum()을 매 반복마다 실행을하니 시간초과가 발생하였다.
##     그래서 처음에만 sum()을 하고 각 반복마다 pop 및 insert되는
##     수를 빼고 더해줬다.
## *문제해결:
##     1. 최대 반복 횟수는 len(queue1)*2+len(queue1)이다.
##        각 queue의 값을 모두 바꾸고 다시 옮기는 과정까지하는 것이
##        최악의 경우이기 떄문이다.
##     2. 이를 넘어선 경우 -1을 return한다.

from collections import deque

def solution(queue1, queue2):
    answer = 0
    length=len(queue1)*2+len(queue1)
    queue1, queue2 = deque(queue1), deque(queue2)

    sum1, sum2 = sum(queue1), sum(queue2)
    while answer<=length:
        if sum1>sum2:
            num=queue1.popleft()
            queue2.append(num)
            sum1-=num
            sum2+=num
        elif sum1<sum2:
            num=queue2.popleft()
            queue1.append(num)
            sum1+=num
            sum2-=num
        else:
            break
        answer+=1

    if answer>length:
        return -1
    return answer
