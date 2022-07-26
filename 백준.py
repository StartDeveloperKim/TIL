import sys
input=sys.stdin.readline

n=int(input())
info=[]
for _ in range(n):
    info.append(list(map(int, input().split())))

info.sort(key=lambda x: (x[1], x[0]))

start_time=info[0][1]
ans=1
for i in range(1, n):
    if info[i][0]>=start_time:
        start_time=info[i][1]
        ans+=1


print(ans)
