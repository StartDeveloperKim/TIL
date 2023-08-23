## 알고리즘
## 1. deque() 자료구조를 이용한다.
## 2. while문을 이용하여 queue에 자료가 없을 때까지 반복한다.
## 3. deque()의 rotate메서드를 이용해 자료를 회전시킨다.
 
from collections import deque
n=int(input())
queue = deque(enumerate(map(int, input().split())))
answer=[]

while queue:
    idx, num = queue.popleft()
    answer.append(idx+1)
    if num>0:
        queue.rotate(-(num-1))
    else:
        queue.rotate(-num)
    print(queue)
print(*answer)
