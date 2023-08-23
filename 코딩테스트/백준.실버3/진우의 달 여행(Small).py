n, m=map(int, input().split())
fuel=[list(map(int, input().split())) for _ in range(n)]

ans=1e9

def solution(x, py, direct, dist, n, m): #필요한 매개변수 현재 행 인덱스, 이전에 진행했던 방향
    global ans

    if x==n:
        ans=min(ans, dist)
        return
    
    dy=[-1, 0, 1]
    for y in dy:
        if direct!=y and 0<=py+y<m:
            solution(x+1, py+y, y, dist+fuel[x][py+y], n, m)
        
for i in range(m):
    solution(1, i, -2, fuel[0][i], n, m) 
print(ans)
