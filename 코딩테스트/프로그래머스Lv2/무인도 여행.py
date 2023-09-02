#  형적인 BFS 문제였다.
#  계속된 Index 오류때문에 해맸는데 이는 내가 limit_x, limit_y 변수값을 잘못 설정했기때문이다.

from collections import deque                

def solution(maps):
    maps= [list(m) for m in maps]
    
    def bfs(s_x, s_y):
        limit_x=len(maps)
        limit_y=len(maps[0])

        result=[int(maps[s_x][s_y])]
        maps[s_x][s_y]='X'
        queue=deque([(s_x, s_y)])

        dx=[-1, 1, 0, 0]
        dy=[0, 0, -1, 1]

        while queue:
            v1, v2 = queue.popleft()
            for x, y in zip(dx, dy):
                nx=v1+x
                ny=v2+y
                if (0<=nx<limit_x and 0<=ny<limit_y) and maps[nx][ny].isdigit():
                    result.append(int(maps[nx][ny]))
                    maps[nx][ny]='X'
                    queue.append([nx, ny])
        return sum(result)
    
    answer = []
    limit_x, limit_y=len(maps), len(maps[0])
    
    for x in range(limit_x):
        for y in range(limit_y):
            if maps[x][y].isdigit():
                result=bfs(x, y)
                answer.append(result)
                
    
    return sorted(answer) if len(answer)>0 else [-1]
