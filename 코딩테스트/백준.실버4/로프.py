import sys
input=sys.stdin.readline

n=int(input())
ropes=[int(input()) for _ in range(n)]

ropes.sort(reverse=True)
ans=0
for i in range(n):
    ans=max(ans, ropes[i]*(i+1))
print(ans)
