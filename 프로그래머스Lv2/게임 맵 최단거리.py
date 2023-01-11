## 알고리즘(BFS활용)
## 1. 시작점을 queue에 넣는다.
## 2. 방문할 수 있는 모든 노드에에 방문하는데
##    이 경우 이전 위치의 값을 다음위치에 더한다.
##    그러면 그것은 노드까지의 거리이다.
## 3. 도착 노드의 값이 1이라면 방문을 하지 못한 것이기에 -1을 반환한다. 
## 4. 1이 아닌 다른 값이라면 도착을 했다는 것이기에 해당 노드의 값을 반환

from collections import deque

def solution(maps):
    answer = 0
    queue=deque([[0, 0]])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    targetX, targetY=len(maps), len(maps[0])

    while queue:
        x, y=queue.popleft()

        for i, j in zip(dx, dy):
            nx=x+i
            ny=y+j
            if (0<=nx<targetX and 0<=ny<targetY) and maps[nx][ny]==1:
                queue.append([nx, ny])
                maps[nx][ny]+=maps[x][y]

    return maps[targetX-1][targetY-1] if maps[targetX-1][targetY-1]!=1 else -1
